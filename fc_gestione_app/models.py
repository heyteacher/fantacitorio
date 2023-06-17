from django.db import models
from django.conf import settings
from django.template.defaultfilters import date
from django.forms import ValidationError
from django.db.models.functions import Lower
from django.urls import reverse
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager


class CaricaManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class Carica(models.Model):
    objects = CaricaManager()
    name = models.CharField(max_length=50, verbose_name='nome', )
    fanfani = models.IntegerField()
    creato_il = models.DateTimeField(auto_now_add=True)
    aggiornato_il = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return '%s (%s fanfani)' % (self.name,self.fanfani) 

    def natural_key(self):
        return (self.name,)
    
    class Meta:
        db_table = 'carica'
        verbose_name_plural = 'cariche'
        constraints = [
            models.UniqueConstraint(
                Lower('name'),
                name='carica_name_unique'),
        ]
        ordering = ('-fanfani',)

class PoliticoManager(CurrentSiteManager):
    def get_by_natural_key(self, name, site):
        return self.get(name=name, site=site)

class Politico(models.Model):
    name = models.CharField(max_length=200, verbose_name='nomimativo', )
    carica = models.ForeignKey(Carica, models.PROTECT, )
    fanfani = models.IntegerField(default=0)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    creato_il = models.DateTimeField(auto_now_add=True)
    aggiornato_il = models.DateTimeField(auto_now=True) 
    
    objects = PoliticoManager()
    def natural_key(self):
        return (self.name,self.site)

    def get_totale_punti(self, from_datetime = None):
        punteggi = self.punteggio_set.all() if from_datetime is None else self.punteggio_set.filter(puntata__data__gt=from_datetime)
        return sum(p.punti for p in punteggi) if len(punteggi) > 0 else 0

    @property
    def totale_punti(self):
        return self.get_totale_punti() 
 
    def __str__(self):
        return '%s (%s fanfani)' % (self.name, self.fanfani)

    def save(self, *args, **kwargs):
        if (self.fanfani is None or int(self.fanfani) <= 0) and not self.carica is None:
            self.fanfani = self.carica.fanfani 
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'politico'
        verbose_name_plural = 'politici'
        constraints = [
            models.UniqueConstraint(
                Lower('name'),
                name='politico_name_unique'),
        ]
        ordering = ('name',)


class LegaManager(CurrentSiteManager):
    def get_by_natural_key(self, name, site):
        return self.get(name=name, site=site)

class Lega(models.Model):
    name = models.CharField(max_length=100, verbose_name='nome', )
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    creato_il = models.DateTimeField(auto_now_add=True)
    aggiornato_il = models.DateTimeField(auto_now=True) 

    objects = LegaManager()
    def natural_key(self):
        return (self.name, self.site)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'lega'
        verbose_name_plural = 'leghe'
        constraints = [
            models.UniqueConstraint(
                Lower('name'),
                name='lega_name_unique'),
        ]
        ordering = ('name',)

class SquadraManager(CurrentSiteManager):
    def get_by_natural_key(self, name, site):
        return self.get(name=name, site=site)

class Squadra(models.Model):
    objects = SquadraManager()
    codice = models.CharField(max_length=20, null=True, blank=True) 
    name = models.CharField(max_length=200, verbose_name='nome', )
    utente = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True, blank=True)
    leader_politico = models.ForeignKey(Politico, models.PROTECT, verbose_name='leader', related_name='leader')
    number_1_politico = models.ForeignKey(Politico, models.PROTECT, db_column='1_politico_id', related_name = 'number_1_politico', verbose_name='1° politico', ) 
    number_2_politico = models.ForeignKey(Politico, models.PROTECT, db_column='2_politico_id', related_name = 'number_2_politico', verbose_name='2° politico',)
    number_3_politico = models.ForeignKey(Politico, models.PROTECT, db_column='3_politico_id', related_name = 'number_3_politico', verbose_name='3° politico',)
    number_4_politico = models.ForeignKey(Politico, models.PROTECT, db_column='4_politico_id', related_name = 'number_4_politico', verbose_name='4° politico',)
    number_5_politico = models.ForeignKey(Politico, models.PROTECT, db_column='5_politico_id', related_name = 'number_5_politico', verbose_name='5° politico',) 
    number_6_politico = models.ForeignKey(Politico, models.PROTECT, db_column='6_politico_id', related_name = 'number_6_politico', verbose_name='6° politico',)
    number_7_politico = models.ForeignKey(Politico, models.PROTECT, db_column='7_politico_id', related_name = 'number_7_politico', verbose_name='7° politico',) 
    number_8_politico = models.ForeignKey(Politico, models.PROTECT, db_column='8_politico_id', related_name = 'number_8_politico', verbose_name='8° politico',) 
    number_9_politico = models.ForeignKey(Politico, models.PROTECT, db_column='9_politico_id', related_name = 'number_9_politico', verbose_name='9° politico',) 
    number_10_politico = models.ForeignKey(Politico, models.PROTECT, db_column='10_politico_id', related_name = 'number_10_politico', verbose_name='10° politico',)
    number_11_politico = models.ForeignKey(Politico, models.PROTECT, db_column='11_politico_id', related_name = 'number_11_politico', verbose_name='11° politico',)
    punti_bonus_squadra = models.IntegerField(default=0)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    creato_il = models.DateTimeField(auto_now_add=True)
    aggiornato_il = models.DateTimeField(auto_now=True) 
 
    def get_absolute_url(self):
        return reverse('squadra-detail')
    
    def get_politici(self):
        return [self.leader_politico, self.number_1_politico, self.number_2_politico, self.number_3_politico, self.number_4_politico, self.number_5_politico, self.number_6_politico, self.number_7_politico, self.number_8_politico, self.number_9_politico, self.number_10_politico, self.number_11_politico, self.site]

    def clean(self):
        politici_names = [p.name for p in self.get_politici() if p != None]

        if len(politici_names) != len(set(politici_names)):
            raise ValidationError('Lo stesso politico è presente più volte')
            
        if self.totale_fanfani > 160:
            raise ValidationError('Superato il limite di 160 Fanfani')

        if self.leader_politico.carica.name not in ('Leader', 'Legend','Premier'):
            raise ValidationError('il leader politico deve avere una carica di Premier, Leader o Legend')

    def natural_key(self):
        return (self.name, self.site)

    @property
    def totale_fanfani(self):
        return  sum(p.fanfani for p in self.get_politici() if p != None)

    @property
    def totale_punti(self):
        return  sum(p.get_totale_punti(self.creato_il) for p in self.get_politici() if p != None)

    @property
    def totale_punti_leader_politico(self):
        return  self.leader_politico.get_totale_punti(self.creato_il) if self.leader_politico != None else 0

    @property
    def totale_punti_politico_1(self):
        return  self.number_1_politico.get_totale_punti(self.creato_il) if self.number_1_politico != None else 0

    @property
    def totale_punti_politico_2(self):
        return  self.number_2_politico.get_totale_punti(self.creato_il) if self.number_2_politico != None else 0

    @property
    def totale_punti_politico_3(self):
        return  self.number_3_politico.get_totale_punti(self.creato_il) if self.number_3_politico != None else 0

    @property
    def totale_punti_politico_4(self):
        return  self.number_4_politico.get_totale_punti(self.creato_il) if self.number_4_politico != None else 0

    @property
    def totale_punti_politico_5(self):
        return  self.number_5_politico.get_totale_punti(self.creato_il) if self.number_5_politico != None else 0

    @property
    def totale_punti_politico_6(self):
        return  self.number_6_politico.get_totale_punti(self.creato_il) if self.number_6_politico != None else 0

    @property
    def totale_punti_politico_7(self):
        return  self.number_7_politico.get_totale_punti(self.creato_il) if self.number_7_politico != None else 0

    @property
    def totale_punti_politico_8(self):
        return  self.number_8_politico.get_totale_punti(self.creato_il) if self.number_8_politico != None else 0

    @property
    def totale_punti_politico_9(self):
        return  self.number_9_politico.get_totale_punti(self.creato_il) if self.number_9_politico != None else 0

    @property
    def totale_punti_politico_10(self):
        return  self.number_10_politico.get_totale_punti(self.creato_il) if self.number_10_politico != None else 0

    @property
    def totale_punti_politico_11(self):
        return  self.number_11_politico.get_totale_punti(self.creato_il) if self.number_11_politico != None else 0

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'squadra'
        verbose_name_plural = 'squadre'
        constraints = [
            models.UniqueConstraint(
                fields=('name', 'leader_politico','number_1_politico','number_2_politico','number_3_politico','number_4_politico','number_5_politico','number_6_politico','number_7_politico','number_8_politico','number_9_politico','number_10_politico','number_11_politico'),
                name='squadra_unique'),
        ]
        ordering = ('creato_il',)


class LegaSquadraManager(models.Manager):
    def get_by_natural_key(self, lega, squadra):
        return self.get(lega=lega, squadra=squadra)

class LegaSquadra(models.Model):
    objects = LegaSquadraManager()
    lega = models.ForeignKey(Lega, models.PROTECT, )
    squadra = models.ForeignKey(Squadra, models.PROTECT, )
    creato_il = models.DateTimeField(auto_now_add=True)
    aggiornato_il = models.DateTimeField(auto_now=True) 
    def natural_key(self):
        return (self.lega.name, self.squadra.name)
    def __str__(self):
       return '%s-%s' % self.natural_key() 
    class Meta:
        db_table = 'lega_squadra'
        verbose_name_plural = 'leghe - squadre'
        unique_together = ['lega', 'squadra']
        ordering = ('lega__name', 'squadra__name')

class PuntataManager(CurrentSiteManager):
    def get_by_natural_key(self, numero, site):
        return self.get(numero, site)

class Puntata(models.Model):
    numero = models.IntegerField(unique=True, )
    data = models.DateTimeField()
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    creato_il = models.DateTimeField(auto_now_add=True)
    aggiornato_il = models.DateTimeField(auto_now=True) 

    objects = PuntataManager()
    def natural_key(self):
        return (self.numero, self.site)

    def __str__(self):
        return str(self.numero) + '° del ' + date(self.data,'D d/m/Y')

    class Meta:
        db_table = 'puntata'
        verbose_name_plural = 'puntate'
        ordering = ('-numero',)

class PunteggioManager(models.Manager):
    def get_by_natural_key(self, numero, puntata, punti):
        return self.get(numero, puntata, punti)

class Punteggio(models.Model):
    politico = models.ForeignKey(Politico, models.PROTECT, )
    puntata = models.ForeignKey(Puntata, models.PROTECT, )
    punti = models.IntegerField()
    name = models.CharField(max_length=200, verbose_name='nomimativo', null=True)
    creato_il = models.DateTimeField(auto_now_add=True)
    aggiornato_il = models.DateTimeField(auto_now=True) 

    objects = PunteggioManager()
    def natural_key(self):
        return (self.politico, self.puntata, self.punti)

    def __str__(self):
        return str(self.puntata) + ' - ' + str(self.politico) + ' - ' + str(self.punti) + ' punti'

    class Meta:
        db_table = 'punteggio'
        verbose_name_plural = 'punteggi'
        ordering = ('-puntata__numero','-aggiornato_il')
