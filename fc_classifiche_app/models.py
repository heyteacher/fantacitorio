from django.db import models
from fc_gestione_app.models import Squadra, Politico, Lega

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
    nome_squadra = models.CharField(max_length=200)
    totale_punti = models.IntegerField()
    class Meta:
        db_table = 'classifica_per_lega'
        verbose_name_plural = 'classifica per lega'
        ordering = ('lega_id','posizione')