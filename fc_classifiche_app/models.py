from django.db import models
from django.db.models import Index
from django.template.defaultfilters import date
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager

class ClassificaPolitico(models.Model):
    posizione = models.IntegerField(primary_key=True)
    nome_politico = models.CharField(max_length=200)
    totale_punti = models.IntegerField()
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    objects = CurrentSiteManager()
  
    class Meta:
        db_table = 'classifica_politico'
        verbose_name_plural = 'classifica politici'
        ordering = ('posizione',)

class ClassificaGenerale(models.Model):
    posizione = models.IntegerField(primary_key=True)
    squadra_id = models.IntegerField()
    codice_squadra = models.CharField(max_length=20, null=True)
    nome_squadra = models.CharField(max_length=200)
    creato_il = models.DateTimeField(null=True)
    totale_punti = models.IntegerField()
    leader_politico = models.CharField(max_length=100, null=True)
    totale_leader_politico = models.IntegerField(default=0)
    politico_1 = models.CharField(max_length=100, null=True)
    totale_politico_1 = models.IntegerField(default=0)
    politico_2 = models.CharField(max_length=100, null=True)
    totale_politico_2 = models.IntegerField(default=0)
    politico_3 = models.CharField(max_length=100, null=True)
    totale_politico_3 = models.IntegerField(default=0)
    politico_4 = models.CharField(max_length=100, null=True)
    totale_politico_4 = models.IntegerField(default=0)
    politico_5 = models.CharField(max_length=100, null=True)
    totale_politico_5 = models.IntegerField(default=0)
    politico_6 = models.CharField(max_length=100, null=True)
    totale_politico_6 = models.IntegerField(default=0)
    politico_7 = models.CharField(max_length=100, null=True)
    totale_politico_7 = models.IntegerField(default=0)
    politico_8 = models.CharField(max_length=100, null=True)
    totale_politico_8 = models.IntegerField(default=0)
    politico_9 = models.CharField(max_length=100, null=True)
    totale_politico_9 = models.IntegerField(default=0)
    politico_10 = models.CharField(max_length=100, null=True)
    totale_politico_10 = models.IntegerField(default=0)
    politico_11 = models.CharField(max_length=100, null=True)
    totale_politico_11 = models.IntegerField(default=0)
    fanfani = models.IntegerField(default=0)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    objects = CurrentSiteManager()
    class Meta:
        db_table = 'classifica_generale'
        verbose_name_plural = 'classifica generale'
        ordering = ('posizione',)
 
class ClassificaPerLega(models.Model):
    posizione = models.IntegerField()
    lega_id = models.IntegerField()
    nome_lega = models.CharField(max_length=100)
    squadra_id = models.IntegerField()
    nome_squadra = models.CharField(max_length=200)
    totale_punti = models.IntegerField()
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    objects = CurrentSiteManager()
    class Meta:
        db_table = 'classifica_per_lega'
        verbose_name_plural = 'classifica per lega'
        ordering = ('lega_id','posizione')

class SquadraPunti(models.Model):
    squadra_id = models.IntegerField()
    squadra_name = models.CharField(max_length=200)
    politico_name = models.CharField(max_length=200)
    puntata_numero = models.IntegerField()
    puntata_data = models.DateTimeField(auto_now_add=True)
    punti = models.IntegerField()
    @property
    def puntata(self):
        return '%s° del %s' % (self.puntata_numero, date(self.puntata_data,'d/m/Y'))

    class Meta:
        db_table = 'squadra_punti'
        verbose_name_plural = 'punti squadra'
        ordering = ('-puntata_numero', '-id')
        indexes = [
            Index(fields = ('squadra_id',), name='squadra_id_idx'),
        ]

class PunteggioPuntata(models.Model):
    puntata_numero = models.IntegerField()
    puntata_data = models.DateTimeField(auto_now_add=True)
    politico_name = models.CharField(max_length=200)
    punti = models.IntegerField()
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    objects = CurrentSiteManager()
    creato_il = models.DateTimeField(auto_now_add=True)
    @property
    def puntata(self):
        return '%s° del %s' % (self.puntata_numero, date(self.puntata_data,'d/m/Y'))

    class Meta:
        db_table = 'punteggio_puntata'
        verbose_name_plural = 'punteggi'
        ordering = ('-creato_il',)
