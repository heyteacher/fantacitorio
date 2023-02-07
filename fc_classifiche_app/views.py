from django_filters.views import FilterView
from django_tables2.paginators import LazyPaginator
from django_tables2 import SingleTableMixin, SingleTableView
from .models import ClassificaGenerale, ClassificaPerLega, ClassificaPolitico, SquadraPunti, PunteggioPuntata 
from .tables import ClassificaGeneraleTable, ClassificaGeneraleFilter, \
                    ClassificaPerLegaTable, ClassificaPerLegaFilter, \
                    ClassificaPoliticoTable, ClassificaPoliticoFilter, \
                    SquadraPuntiTable, PunteggioPuntataTable, PunteggioPuntataFilter

class ClassificaGeneraleListView(SingleTableMixin, FilterView):
    model = ClassificaGenerale
    table_class = ClassificaGeneraleTable
    template_name = 'table.html'
    filterset_class = ClassificaGeneraleFilter
    pagination_class = LazyPaginator
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_plural_name'] = 'squadre'
        return context

class ClassificaPerLegaListView(SingleTableMixin, FilterView):
    model = ClassificaPerLega
    table_class = ClassificaPerLegaTable
    template_name = 'table.html'
    filterset_class = ClassificaPerLegaFilter
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_plural_name'] = 'squadre'
        return context

class ClassificaPoliticoListView(SingleTableMixin, FilterView):
    model = ClassificaPolitico
    table_class = ClassificaPoliticoTable
    template_name = 'table.html'
    filterset_class = ClassificaPoliticoFilter
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_plural_name'] = 'politici'
        return context

class SquadraPuntiListView(SingleTableView):
    table_class = SquadraPuntiTable
    template_name = 'dettaglio_squadra.html'
    table_pagination = False
    
    def get_queryset(self):
        return SquadraPunti.objects.filter(squadra_id=self.kwargs['squadra_id'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classifica'] = ClassificaGenerale.objects.get(squadra_id=self.kwargs['squadra_id'])
        context['classifica_leghe'] = ClassificaPerLega.objects.filter(squadra_id=self.kwargs['squadra_id'])
        context['entity_plural_name'] = 'punteggi'
        return context

class PunteggioPuntataListView(SingleTableMixin, FilterView):
    model = PunteggioPuntata
    table_class = PunteggioPuntataTable
    template_name = 'table.html'
    filterset_class = PunteggioPuntataFilter
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_plural_name'] = 'punteggi'
        return context