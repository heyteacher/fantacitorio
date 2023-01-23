from django.db import models
from django.db.models import Index
from django.template.defaultfilters import date

class ClassificaPolitico(models.Model):
    posizione = models.IntegerField(primary_key=True)
    nome_politico = models.CharField(max_length=200)
    totale_punti = models.IntegerField()  
    class Meta:
        db_table = 'classifica_politico'
        verbose_name_plural = 'classifica politici'
        ordering = ('posizione',)

class ClassificaGenerale(models.Model):
    posizione = models.IntegerField(primary_key=True)
    squadra_id = models.IntegerField()
    nome_squadra = models.CharField(max_length=200)
    totale_punti = models.IntegerField()
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
        return '%s ° del %s' % (self.puntata_numero, date(self.puntata_data,'D d/m/Y'))

    class Meta:
        db_table = 'squadra_punti'
        verbose_name_plural = 'punti squadra'
        ordering = ('puntata_numero',)
        indexes = [
            Index(fields = ('squadra_id',), name='squadra_id_idx'),
        ]
