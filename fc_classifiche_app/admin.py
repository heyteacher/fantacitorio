from django.contrib import admin
from admin_auto_filters.filters import AutocompleteFilter
from fc_classifiche_app.models import ClassificaGenerale, ClassificaPerLega, ClassificaPolitico
from import_export import resources
from import_export.admin import ExportActionMixin

class PoliticoFilter(AutocompleteFilter):
    title = 'Politico' # display title
    field_name = 'politico' # name of the foreign key field

class SquadraFilter(AutocompleteFilter):
    title = 'Squadra' # display title
    field_name = 'squadra' # name of the foreign key field

class LegaFilter(AutocompleteFilter):
    title = 'Lega' # display title
    field_name = 'lega' # name of the foreign key field

class ClassificaPoliticoResource(resources.ModelResource):
    class Meta:
        model = ClassificaPolitico
        skip_unchanged = True   
        report_skipped = False        
        fields = ('posizione', 'politico__name','totale_punti')

@admin.register(ClassificaPolitico)
class ClassificaPoliticoAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_classes = [ClassificaPoliticoResource]
    list_display = ('posizione', 'politico', 'totale_punti')
    readonly_fields= ('posizione', 'politico', 'totale_punti')
    ordering = ('posizione', 'politico', 'totale_punti')
    list_filter = (PoliticoFilter,)
    autocomplete_fields = ('politico',)
    search_fields = ('politico__name',) 
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
        fields = ('posizione', 'squadra__name','totale_punti')

@admin.register(ClassificaGenerale)
class ClassificaGeneraleAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_classes = [ClassificaGeneraleResource]
    list_display = ('posizione', 'squadra', 'totale_punti')
    ordering = ('posizione', 'squadra', 'totale_punti')
    readonly_fields= ('posizione', 'squadra', 'totale_punti')
    list_filter = (SquadraFilter,)
    autocomplete_fields = ('squadra',)
    search_fields = ('squadra__name',) 
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
        fields = ('lega__name', 'posizione', 'squadra__name','totale_punti')

@admin.register(ClassificaPerLega)
class ClassificaPerLegaAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_classes = [ClassificaPerLegaResource]
    model = ClassificaPerLega
    list_display = ('lega', 'posizione', 'squadra', 'totale_punti')
    list_display_links = None
    search_fields = ('lega__name','squadra__name')
    list_filter = (LegaFilter, SquadraFilter)

    pos = 0
 
    def __init__(self, parent_model, admin_site) :
        super().__init__(parent_model, admin_site)
        self._pos = 0
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def pos(self, obj):
        self._pos += 1
        return self._pos