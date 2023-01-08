from django_filters.views import FilterView
from django_tables2.paginators import LazyPaginator
from django_tables2 import SingleTableMixin
from .models import ClassificaGenerale, ClassificaPerLega, ClassificaPolitico
from .tables import ClassificaGeneraleTable, ClassificaGeneraleFilter, \
                    ClassificaPerLegaTable, ClassificaPerLegaFilter, \
                    ClassificaPoliticoTable, ClassificaPoliticoFilter

class ClassificaGeneraleListView(SingleTableMixin, FilterView):
    model = ClassificaGenerale
    table_class = ClassificaGeneraleTable
    template_name = 'table.html'
    filterset_class = ClassificaGeneraleFilter
    pagination_class = LazyPaginator

class ClassificaPerLegaListView(SingleTableMixin, FilterView):
    model = ClassificaPerLega
    table_class = ClassificaPerLegaTable
    template_name = 'table.html'
    filterset_class = ClassificaPerLegaFilter

class ClassificaPoliticoListView(SingleTableMixin, FilterView):
    model = ClassificaPolitico
    table_class = ClassificaPoliticoTable
    template_name = 'table.html'
    filterset_class = ClassificaPoliticoFilter