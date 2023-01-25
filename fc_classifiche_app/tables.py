import django_tables2 as tables
from django_tables2.utils import A
import django_tables2.paginators as LazyPaginator
from .models import ClassificaGenerale, ClassificaPerLega, ClassificaPolitico, SquadraPunti
from django_filters import FilterSet, CharFilter, ChoiceFilter
from fc_gestione_app.models import Lega

template_name = "django_tables2/bootstrap5.html"
per_page = 15
attrs =  {
    "class": "table table-dark table-bordered  table-striped table-sm ",
}

class ClassificaGeneraleFilter(FilterSet):
    nome_squadra = CharFilter('nome_squadra','icontains' , label="Nome squadra")
    class Meta:
        model = ClassificaGenerale
        fields = ['nome_squadra']

class ClassificaGeneraleTable(tables.Table):
    nome_squadra = tables.LinkColumn("squadra_punti", args=[A("squadra_id")])
    class Meta:
        model = ClassificaGenerale
        template_name = template_name
        per_page = per_page
        attrs = attrs
        paginator_class = LazyPaginator
        fields = ['posizione', 'nome_squadra', 'totale_punti']

class ClassificaPerLegaFilter(FilterSet):
    lega_id = ChoiceFilter(choices=Lega.objects.all().values_list('id','name'), empty_label="- Seleziona una lega -")
    nome_squadra = CharFilter('nome_squadra','icontains' , label="Nome squadra")
    class Meta:
        model = ClassificaPerLega
        fields = ['lega_id','nome_squadra']

class ClassificaPerLegaTable(tables.Table):
    nome_squadra = tables.LinkColumn("squadra_punti", args=[A("squadra_id")])
    class Meta:
        model = ClassificaPerLega
        template_name = template_name
        per_page = per_page
        attrs = attrs
        exclude = ['id','lega_id', 'squadra_id']

class ClassificaPoliticoFilter(FilterSet):
    nome_politico = CharFilter('nome_politico','icontains' , label="Nome politico")
    class Meta:
        model = ClassificaPolitico
        fields = ['nome_politico']

class ClassificaPoliticoTable(tables.Table):
    class Meta:
        model = ClassificaPolitico
        template_name = template_name
        per_page = per_page
        attrs = attrs

class SquadraPuntiTable(tables.Table):
    class Meta:
        model = SquadraPunti
        template_name = template_name
        #per_page = per_page
        attrs = attrs
        fields = ['puntata', 'politico_name', 'punti']
