import django_tables2 as tables
from .models import Punteggio

template_name = "django_tables2/bootstrap5.html"
attrs =  {
    "class": "table table-dark table-bordered  table-striped table-sm ",
}

class PunteggiTable(tables.Table):
    puntata = tables.Column(order_by=("puntata__data"))
    politico__name = tables.Column(order_by=("politico__name"),verbose_name="Politico")
    class Meta:
        model = Punteggio
        template_name = template_name
        attrs = attrs
        fields = ['puntata', 'politico__name', 'punti']
