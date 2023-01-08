import django_tables2 as tables
from .models import ClassificaGenerale, ClassificaPerLega, ClassificaPolitico
from django_filters import FilterSet, CharFilter, ModelChoiceFilter
from fc_gestione_app.models import Lega

template_name = "django_tables2/bootstrap.html"
per_page = 20
attrs =  {"class": "table table-bordered  table-striped table-condensed"}

class ClassificaGeneraleFilter(FilterSet):
    nome_squadra = CharFilter('squadra__name','icontains' , label="Nome squadra")
    class Meta:
        model = ClassificaGenerale
        fields = ['nome_squadra']

class ClassificaGeneraleTable(tables.Table):
    class Meta:
        model = ClassificaGenerale
        template_name = template_name
        per_page = per_page
        attrs = attrs

class ClassificaPerLegaFilter(FilterSet):
    lega = ModelChoiceFilter(queryset=Lega.objects.all(), empty_label="- Seleziona una lega -")
    nome_squadra = CharFilter('squadra__name','icontains' , label="Nome squadra")
    class Meta:
        model = ClassificaPerLega
        fields = ['lega','nome_squadra']

class ClassificaPerLegaTable(tables.Table):
    class Meta:
        model = ClassificaPerLega
        template_name = template_name
        per_page = per_page
        attrs = attrs
        exclude = ["id"]

class ClassificaPoliticoFilter(FilterSet):
    nome_politico = CharFilter('politico__name','icontains' , label="Nome politico")
    class Meta:
        model = ClassificaPolitico
        fields = ['nome_politico']

class ClassificaPoliticoTable(tables.Table):
    class Meta:
        model = ClassificaPolitico
        template_name = template_name
        per_page = per_page
        attrs = attrs
