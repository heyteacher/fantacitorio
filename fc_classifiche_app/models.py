from django.db import models
from fc_gestione_app.models import Squadra, Politico, Lega

class ClassificaPolitico(models.Model):
    posizione = models.IntegerField(primary_key=True)
    politico = models.ForeignKey(Politico, models.DO_NOTHING, )
    totale_punti = models.IntegerField()  
    class Meta:
        managed = False
        db_table = 'v_classifica_politico'
        verbose_name_plural = 'classifica politici'

class ClassificaGenerale(models.Model):
    posizione = models.IntegerField(primary_key=True)
    squadra = models.ForeignKey(Squadra, models.DO_NOTHING, )
    totale_punti = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'v_classifica_generale'
        verbose_name_plural = 'classifica generale'

class ClassificaPerLega(models.Model):
    posizione = models.IntegerField()
    lega = models.ForeignKey(Lega, models.DO_NOTHING, )
    squadra = models.ForeignKey(Squadra, models.DO_NOTHING, )
    totale_punti = models.IntegerField()

    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'v_classifica_per_lega'
        verbose_name_plural = 'classifica per lega'
        unique_together = (('lega', 'squadra'),)
        ordering = ['lega__name','posizione']