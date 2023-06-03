from django.contrib import admin
from fc_classifiche_app.models import ClassificaGenerale, ClassificaPerLega, ClassificaPolitico, PunteggioPuntata
from import_export import resources
from import_export.admin import ExportActionMixin

class ClassificaPoliticoResource(resources.ModelResource):
    class Meta:
        model = ClassificaPolitico
        skip_unchanged = True   
        report_skipped = False        
        fields = ('posizione', 'nome_politico','totale_punti')

@admin.register(ClassificaPolitico)
class ClassificaPoliticoAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_classes = [ClassificaPoliticoResource]
    list_display = ('posizione', 'nome_politico', 'totale_punti')
    readonly_fields= ('posizione', 'nome_politico', 'totale_punti')
    search_fields = ('nome_politico',) 
    actions = None
 
    list_display_links = None
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def posizione(self, obj):
        self._posizione += 1
        return self._posizione

class ClassificaGeneraleResource(resources.ModelResource):
    class Meta:
        model = ClassificaGenerale
        skip_unchanged = True   
        report_skipped = False        
        fields = ('posizione', 'nome_squadra','totale_punti')
@admin.register(ClassificaGenerale)
class ClassificaGeneraleAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_classes = [ClassificaGeneraleResource]
    list_display = ('posizione', 'nome_squadra', 'totale_punti')
    readonly_fields= ('posizione', 'nome_squadra', 'totale_punti')
    search_fields = ('nome_squadra',) 
    actions = None
    list_display_links = None

    def __init__(self, parent_model, admin_site) :
        super().__init__(parent_model, admin_site)
        self._posizione = 0

    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def posizione(self, obj):
        self._posizione += 1
        return self._posizione

class ClassificaPerLegaResource(resources.ModelResource):
    class Meta:
        model = ClassificaPerLega
        skip_unchanged = True   
        report_skipped = False        
        fields = ('nome_lega', 'posizione', 'nome_squadra','totale_punti')

@admin.register(ClassificaPerLega)
class ClassificaPerLegaAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_classes = [ClassificaPerLegaResource]
    model = ClassificaPerLega
    list_display = ('nome_lega', 'posizione', 'nome_squadra', 'totale_punti')
    list_display_links = None
    search_fields = ('nome_lega','nome_squadra')
    
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False


class PunteggioPuntataResource(resources.ModelResource):
    class Meta:
        model = PunteggioPuntata
        skip_unchanged = True
        report_skipped = False
        fields = ('puntata_numero', 'puntata_data', 'politico_name','punti')

@admin.register(PunteggioPuntata)
class PunteggioPuntataAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_classes = [PunteggioPuntataResource]
    model = PunteggioPuntata
    list_display = ('puntata_numero', 'puntata_data', 'politico_name','punti')
    list_display_links = None
    search_fields = ('puntata_numero','politico_name')
    
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
