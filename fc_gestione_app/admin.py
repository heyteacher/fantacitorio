from django.contrib import admin
from django import forms
from import_export.admin import ImportExportActionModelAdmin

from .models import Carica, Lega, LegaSquadra, Politico, Puntata, Punteggio, Squadra
from .filters import CaricaFilter, LegaFilter, PuntataFilter, SquadraFilter, PoliticoFilter
from .import_export_resources import CaricaResource, LegaResource, LegaSquadraResource, PoliticoResource, PuntataResource,PunteggioResource,SquadraResource

admin.ModelAdmin.save_on_top=True
admin.ModelAdmin.save_as = True

admin.site.site_title  =  "Fantacitorio"
admin.site.index_title  =  "Fantacitorio"

class PoliticoInline(admin.TabularInline):
    model = Politico
    readonly_fields = ('name',)
    extra = 0

@admin.register(Carica)
class CaricaAdmin(ImportExportActionModelAdmin):
    resource_classes = [CaricaResource]
    list_display = ('name', 'fanfani')
    search_fields =('name',)
    inlines = [
        PoliticoInline,
    ]

class PunteggioPoliticoInline(admin.TabularInline):
    model = Punteggio
    fields = ('puntata', 'punti')
    readonly_fields = ('puntata', 'punti')
    extra = 0

@admin.register(Politico)
class PoliticoAdmin(ImportExportActionModelAdmin):
    resource_classes = [PoliticoResource]
    list_display = ('name', 'carica', 'totale_punti')
    fields = ('name', 'carica', 'fanfani')
    readonly_fields = ('totale_punti',)
    list_filter = (CaricaFilter,)
    search_fields = ('name', 'carica__name')
    autocomplete_fields = ['carica',]
    inlines = [
        PunteggioPoliticoInline,
    ]

class LegaSquadraInline(admin.TabularInline):
    model = LegaSquadra
    list_display = ('squadra',)
    autocomplete_fields = ['squadra',]    
    extra = 0

@admin.register(Lega)
class LegaAdmin(ImportExportActionModelAdmin):
    resource_classes = [LegaResource]
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [
        LegaSquadraInline,
    ]

class SquadraAdminForm( forms.ModelForm ):
    def __init__(self, *args, **kwargs):
        super(SquadraAdminForm, self).__init__(*args, **kwargs)
        try:
            if 'leader_politico' in self.fields:
                self.fields['leader_politico'].queryset = self.fields['leader_politico'].queryset.filter(carica__name__in= ('Leader','Legend')) 
        except Exception as err:
            if 'leader_politico' in self.fields:
                self.fields['leader_politico'].queryset = Politico.objects.none()

@admin.register(Squadra)
class SquadraAdmin(ImportExportActionModelAdmin):
    form = SquadraAdminForm
    resource_classes = [SquadraResource]
    list_display = ('name', 'codice','totale_fanfani','leader_politico','creato_il')
    fields = (
        ('name', 'codice'), 
        ('leader_politico', 'number_1_politico'), 
        ('number_2_politico', 'number_3_politico'), 
        ('number_4_politico', 'number_5_politico'), 
        ('number_6_politico', 'number_7_politico'), 
        ('number_8_politico', 'number_9_politico'), 
        ('number_10_politico', 'number_11_politico'), 
        ('punti_bonus_squadra' ,'utente'), 
        ('totale_fanfani', 'creato_il', 'aggiornato_il'), 
    )
    readonly_fields = ('totale_fanfani','creato_il', 'aggiornato_il', 'codice')
    #list_filter = (,)
    autocomplete_fields = ('number_1_politico','number_2_politico','number_3_politico','number_4_politico','number_5_politico','number_6_politico','number_7_politico','number_8_politico','number_9_politico','number_10_politico','number_11_politico', )
    search_fields = ('name', 'codice')
    inlines = [
        LegaSquadraInline,
    ]

    def save_model(self, request, obj, form, change):
        if obj.utente is None:
            obj.utente = request.user
        super().save_model(request, obj, form, change)

@admin.register(LegaSquadra)
class LegaSquadraAdmin(ImportExportActionModelAdmin):
    resource_classes = [LegaSquadraResource]
    list_display = ('lega', 'squadra')
    list_filter = (LegaFilter, SquadraFilter)
    autocomplete_fields = ('lega', 'squadra')
    search_fields = ('lega__name', 'squadra__name',) 

class PunteggioAdminForm( forms.ModelForm ):
    def __init__(self, *args, **kwargs):
        super(PunteggioAdminForm, self).__init__(*args, **kwargs)
        try:
            if 'puntata' in self.fields:
                self.fields['puntata'].initial = Puntata.objects.latest('data')
        except Exception as err:
            pass

class PunteggioPuntataInline(admin.TabularInline):
    model = Punteggio
    fields = ('politico','punti')
    #readonly_fields = ('politico','punti')
    extra = 0

@admin.register(Puntata)
class PuntataAdmin(ImportExportActionModelAdmin):
    resource_classes = [PuntataResource]
    search_fields = ('numero', 'data')
    inlines = [
        PunteggioPuntataInline,
    ]

@admin.register(Punteggio)
class PunteggioAdmin(ImportExportActionModelAdmin):
    form = PunteggioAdminForm
    resource_classes = [PunteggioResource]
    list_display = ('puntata', 'politico', 'punti')
    exclude = ('name',)
    list_filter = (PoliticoFilter, PuntataFilter,)
    autocomplete_fields = ('politico', 'puntata')
    search_fields = ('politico__name',) 