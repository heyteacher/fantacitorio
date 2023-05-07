from import_export import resources, fields, widgets
from import_export.admin import ImportExportActionModelAdmin
from .models import Carica, Lega, LegaSquadra, Politico, Puntata, Punteggio, Squadra

class CaricaResource(resources.ModelResource):
    class Meta:
        model = Carica
        skip_unchanged = True
        exclude = ('id','creato_il', 'aggiornato_il')
        import_id_fields = ('name',)

class PoliticoResource(resources.ModelResource):
    name = fields.Field(
        column_name='name',
        attribute='name')
    carica = fields.Field(
        column_name='carica',
        attribute='carica',
        widget=widgets.ForeignKeyWidget(model=Carica, field='name'))
    fanfani = fields.Field(
        column_name='fanfani',
        attribute='fanfani')
    class Meta:
        model = Politico
        skip_unchanged = True
        exclude = ('id', 'creato_il', 'aggiornato_il')
        import_id_fields = ('name',)

class LegaResource(resources.ModelResource):
    class Meta:
        model = Lega
        exclude = ('id', 'creato_il', 'aggiornato_il')
        skip_unchanged = True
        import_id_fields = ('name',)

class SquadraResource(resources.ModelResource):
    codice = fields.Field(
        column_name='codice',
        attribute='codice')
    name = fields.Field(
        column_name='name',
        attribute='name')
    punti_bonus_squadra = fields.Field(
        column_name='punti_bonus_squadra',
        attribute='punti_bonus_squadra')
    leader_politico = fields.Field(
        column_name='leader_politico',
        attribute='leader_politico',
        widget=widgets.ForeignKeyWidget(Politico, field='name'))
    number_1_politico = fields.Field(
        column_name='number_1_politico',
        attribute='number_1_politico',
        widget=widgets.ForeignKeyWidget(Politico, field='name'))
    number_2_politico = fields.Field(
        column_name='number_2_politico',
        attribute='number_2_politico',
        widget=widgets.ForeignKeyWidget(Politico, field='name'))
    number_3_politico = fields.Field(
        column_name='number_3_politico',
        attribute='number_3_politico',
        widget=widgets.ForeignKeyWidget(Politico, field='name'))
    number_4_politico = fields.Field(
        column_name='number_4_politico',
        attribute='number_4_politico',
        widget=widgets.ForeignKeyWidget(Politico, field='name'))
    number_5_politico = fields.Field(
        column_name='number_5_politico',
        attribute='number_5_politico',
        widget=widgets.ForeignKeyWidget(Politico, field='name'))
    number_6_politico = fields.Field(
        column_name='number_6_politico',
        attribute='number_6_politico',
        widget=widgets.ForeignKeyWidget(Politico, field='name'))
    number_7_politico = fields.Field(
        column_name='number_7_politico',
        attribute='number_7_politico',
        widget=widgets.ForeignKeyWidget(Politico, field='name'))
    number_8_politico = fields.Field(
        column_name='number_8_politico',
        attribute='number_8_politico',
        widget=widgets.ForeignKeyWidget(Politico, field='name'))
    number_9_politico = fields.Field(
        column_name='number_9_politico',
        attribute='number_9_politico',
        widget=widgets.ForeignKeyWidget(Politico, field='name'))
    number_10_politico = fields.Field(
        column_name='number_10_politico',
        attribute='number_10_politico',
        widget=widgets.ForeignKeyWidget(Politico, field='name'))
    number_11_politico = fields.Field(
        column_name='number_11_politico',
        attribute='number_11_politico',
        widget=widgets.ForeignKeyWidget(Politico, field='name'))
    creato_il = fields.Field(
        column_name='creato_il',
        attribute='creato_il',
        widget=widgets.DateTimeWidget(format='%d/%m/%Y %H:%M'))
    class Meta:
        model = Squadra
        skip_unchanged = True
        report_skipped = False
        exclude = ('id','utente','aggiornato_il')
        import_id_fields = ('name', 'leader_politico','number_1_politico','number_2_politico','number_3_politico','number_4_politico','number_5_politico','number_6_politico','number_7_politico','number_8_politico','number_9_politico','number_10_politico','number_11_politico')

class LegaSquadraResource(resources.ModelResource):
    lega = fields.Field(
        column_name='lega',
        attribute='lega',
        widget=widgets.ForeignKeyWidget(model=Lega, field='name'))
    squadra = fields.Field(
        column_name='squadra',
        attribute='squadra',
        widget=widgets.ForeignKeyWidget(model=Squadra, field='name'))
    class Meta:
        model = LegaSquadra
        skip_unchanged = True
        exclude = ('id', 'creato_il','aggiornato_il')
        import_id_fields = ('lega', 'squadra')

class PuntataResource(resources.ModelResource):
    class Meta:
        model = Puntata
        skip_unchanged = True
        exclude = ('id', 'creato_il','aggiornato_il')
        import_id_fields = ('numero', 'data')

class PunteggioResource(resources.ModelResource):
    politico = fields.Field(
        column_name='politico',
        attribute='politico',
        widget=widgets.ForeignKeyWidget(Politico, field='name'))
    puntata = fields.Field(
        column_name='puntata',
        attribute='puntata',
        widget=widgets.ForeignKeyWidget(Puntata, field='numero'))
    class Meta:
        model = Punteggio
        skip_unchanged = True
        import_id_fields = ('politico', 'puntata', 'punti')
        exclude = ('id','creato_il','aggiornato_il','name')
