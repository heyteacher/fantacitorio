import django_tables2 as tables
from django_tables2.utils import A
import django_tables2.paginators as LazyPaginator
from .models import ClassificaGenerale, ClassificaPerLega, ClassificaPolitico, SquadraPunti, PunteggioPuntata
from django_filters import FilterSet, CharFilter, ChoiceFilter
from fc_gestione_app.models import Lega, Puntata

template_name = "django_tables2/bootstrap5.html"
per_page = 15
attrs =  {
    "class": "table table-dark table-bordered  table-striped table-sm ",
}

class ClassificaGeneraleFilter(FilterSet):
    squadra = CharFilter('nome_squadra','icontains' , label="squadra")
    class Meta:
        model = ClassificaGenerale
        fields = ['squadra']

def disqualified_row_attrs(**kwargs):
    record = kwargs.get('record', None)
    tr_class = ''
    if record:
        if record.fanfani > 160:
            tr_class = 'disqualified'
    return tr_class

class ClassificaGeneraleTable(tables.Table):
    nome_squadra = tables.LinkColumn("squadra_punti", args=[A("squadra_id")])
    class Meta:
        model = ClassificaGenerale
        template_name = template_name
        per_page = per_page
        attrs = attrs
        paginator_class = LazyPaginator
        fields = ['posizione', 'nome_squadra', 'totale_punti']
        row_attrs = {'class': disqualified_row_attrs}

class ClassificaPerLegaFilter(FilterSet):
    lega_id = ChoiceFilter(choices=Lega.objects.all().values_list('id','name'), empty_label="- Seleziona lega -")
    squadra = CharFilter('nome_squadra','icontains' , label="squadra")
    class Meta:
        model = ClassificaPerLega
        fields = ['lega_id','squadra']

class ClassificaPerLegaTable(tables.Table):
    nome_squadra = tables.LinkColumn("squadra_punti", args=[A("squadra_id")])
    class Meta:
        model = ClassificaPerLega
        template_name = template_name
        per_page = per_page
        attrs = attrs
        exclude = ['id','lega_id', 'squadra_id', 'site']

class ClassificaPoliticoFilter(FilterSet):
    politico = CharFilter('nome_politico','icontains' , label="politico")
    class Meta:
        model = ClassificaPolitico
        fields = ['politico']

class ClassificaPoliticoTable(tables.Table):
    nome_politico =  tables.TemplateColumn('<a href="{% url "punteggio_puntata" %}?politico={{record.nome_politico }}">{{record.nome_politico}}</a>')
    class Meta:
        model = ClassificaPolitico
        template_name = template_name
        per_page = per_page
        attrs = attrs
        exclude = ['site']

def loadPuntate():
    try:
        return [(puntata.numero, puntata) for puntata in Puntata.objects.all()]
    except:
        pass

class PunteggioPuntataFilter(FilterSet):
    puntata_numero = ChoiceFilter(choices=loadPuntate(), empty_label="- Seleziona puntata -")
    politico = CharFilter('politico_name','icontains' , label="politico")

    class Meta:
        model = PunteggioPuntata
        fields = ['puntata_numero','politico']

class PunteggioPuntataTable(tables.Table):
    puntata = tables.Column(order_by=("puntata_data"))
    class Meta:
        model = PunteggioPuntata
        template_name = template_name
        per_page = per_page
        attrs = attrs
        fields = ['puntata', 'politico_name', 'punti']

class SquadraPuntiTable(tables.Table):
    puntata = tables.Column(order_by=("puntata_data"))
    class Meta:
        model = SquadraPunti
        template_name = template_name
        #per_page = per_page
        attrs = attrs
        fields = ['puntata', 'politico_name', 'punti']
