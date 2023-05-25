from django.views import View
from django.views.decorators.cache import never_cache, cache_page
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.core.management import call_command
from django.contrib.auth.mixins import PermissionRequiredMixin
from django_filters.views import FilterView
from django_tables2.paginators import LazyPaginator
from django_tables2 import SingleTableMixin, SingleTableView
from .models import ClassificaGenerale, ClassificaPerLega, ClassificaPolitico, SquadraPunti, PunteggioPuntata 
from .tables import ClassificaGeneraleTable, ClassificaGeneraleFilter, \
                    ClassificaPerLegaTable, ClassificaPerLegaFilter, \
                    ClassificaPoliticoTable, ClassificaPoliticoFilter, \
                    SquadraPuntiTable, PunteggioPuntataTable, PunteggioPuntataFilter

def_cache_page = cache_page(600)
#def_cache_page = never_cache

class NoIndexRobotsMixin:
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        response['X-Robots-Tag'] = 'noindex'
        #print('noindex', request.path)
        return response


class NoIndexRobotsPageSortMixin:
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if 'page' in  request.GET or 'sort' in  request.GET:
            response['X-Robots-Tag'] = 'noindex'
            #print('noindex sortpage', request.path, request.GET)
        return response

@method_decorator(def_cache_page, name='get')
class ClassificaGeneraleListView(NoIndexRobotsPageSortMixin, SingleTableMixin, FilterView):
    model = ClassificaGenerale
    table_class = ClassificaGeneraleTable
    template_name = 'fc_classifiche_app/table.html'
    filterset_class = ClassificaGeneraleFilter
    pagination_class = LazyPaginator
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_plural_name'] = 'squadre'
        return context

@method_decorator(def_cache_page, name='get')
class ClassificaPerLegaListView(NoIndexRobotsMixin, SingleTableMixin, FilterView):
    model = ClassificaPerLega
    table_class = ClassificaPerLegaTable
    template_name = 'fc_classifiche_app/table.html'
    filterset_class = ClassificaPerLegaFilter
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_plural_name'] = 'squadre'
        return context

@method_decorator(def_cache_page, name='get')
class ClassificaPoliticoListView(NoIndexRobotsPageSortMixin, SingleTableMixin, FilterView):
    model = ClassificaPolitico
    table_class = ClassificaPoliticoTable
    template_name = 'fc_classifiche_app/table.html'
    filterset_class = ClassificaPoliticoFilter
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_plural_name'] = 'politici'
        return context

@method_decorator(def_cache_page, name='get')
class SquadraPuntiListView(NoIndexRobotsMixin, SingleTableView):
    table_class = SquadraPuntiTable
    template_name = 'fc_classifiche_app/dettaglio_squadra.html'
    table_pagination = False
    
    def get_queryset(self):
        return SquadraPunti.objects.filter(squadra_id=self.kwargs['squadra_id'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classifica'] = ClassificaGenerale.objects.get(squadra_id=self.kwargs['squadra_id'])
        context['classifica_leghe'] = ClassificaPerLega.objects.filter(squadra_id=self.kwargs['squadra_id'])
        context['entity_plural_name'] = 'punteggi'
        return context

@method_decorator(def_cache_page, name='get')
class PunteggioPuntataListView(NoIndexRobotsPageSortMixin, SingleTableMixin, FilterView):
    model = PunteggioPuntata
    table_class = PunteggioPuntataTable
    template_name = 'fc_classifiche_app/table.html'
    filterset_class = PunteggioPuntataFilter
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_plural_name'] = 'punteggi'
        return context

@method_decorator(never_cache, name='get')
class RefreshClassificheView(NoIndexRobotsMixin, PermissionRequiredMixin,View):
    template_name = 'fc_classifiche_app/refresh_classifiche.html'
    permission_required = 'fc_classifiche_app.change_classificagenerale'
    raise_exception = True

    def get(self, request, *args, **kwargs):
        output_rows = call_command('sqlite_refresh_classifiche','--force').split("\n")
        return render(request, self.template_name, {'output_rows': output_rows})