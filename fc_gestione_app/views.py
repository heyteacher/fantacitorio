from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from dal import autocomplete
from .models import Squadra, Politico, Punteggio
from fc_classifiche_app.models import ClassificaGenerale, ClassificaPerLega
import djhacker 
from django import forms
from django_tables2 import SingleTableMixin
from .tables import PunteggiTable
from django.db.models import Q

fields = [
    'name',
    'leader_politico',
    'number_1_politico',
    'number_2_politico',
    'number_3_politico',
    'number_4_politico',
    'number_5_politico',
    'number_6_politico',
    'number_7_politico',
    'number_8_politico',
    'number_9_politico',
    'number_10_politico',
    'number_11_politico',
]

class SquadraCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/twitter/login/?process=login'
    model = Squadra
    fields = fields

class SquadraUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/twitter/login/?process=login'
    model = Squadra
    fields = fields

    def get_object(self):
        return Squadra.objects.get(id = self.request.session.get('squadra_id'))

class SquadraDetailView(LoginRequiredMixin, SingleTableMixin, DetailView):
    login_url = '/accounts/twitter/login/?process=login'
    table_class = PunteggiTable
    model = Squadra
    template_name = 'fc_gestione_app/dettaglio_squadra.html'

    def get_object(self):
        return Squadra.objects.get(id = self.request.session.get('squadra_id'))

    def get_table_data(self):
        squadra = self.get_object()
        return Punteggio.objects.filter(puntata__data__gt=squadra.creato_il).filter(
                Q(politico=squadra.leader_politico) |
                Q(politico=squadra.number_1_politico) |
                Q(politico=squadra.number_2_politico) |
                Q(politico=squadra.number_3_politico) |
                Q(politico=squadra.number_4_politico) |
                Q(politico=squadra.number_5_politico) |
                Q(politico=squadra.number_6_politico) |
                Q(politico=squadra.number_7_politico) |
                Q(politico=squadra.number_8_politico) |
                Q(politico=squadra.number_9_politico) |
                Q(politico=squadra.number_10_politico)|
                Q(politico=squadra.number_11_politico) 
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['classifica'] = ClassificaGenerale.objects.get(squadra_id=self.request.session.get('squadra_id'))
        context['classifica_leghe'] = ClassificaPerLega.objects.filter(squadra_id=self.request.session.get('squadra_id'))
        context['entity_plural_name'] = 'punteggi'
        return context


class PoliticoAutocompleteView(LoginRequiredMixin,autocomplete.Select2QuerySetView):
    login_url = '/accounts/twitter/login/?process=login'

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Politico.objects.none()
        qs = Politico.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs

djhacker.formfield(
    Squadra.leader_politico,
    forms.ModelChoiceField,
    widget=autocomplete.ModelSelect2(url='politico-autocomplete')
)
djhacker.formfield(
    Squadra.number_1_politico,
    forms.ModelChoiceField,
    widget=autocomplete.ModelSelect2(url='politico-autocomplete')
)
djhacker.formfield(
    Squadra.number_2_politico,
    forms.ModelChoiceField,
    widget=autocomplete.ModelSelect2(url='politico-autocomplete')
)
djhacker.formfield(
    Squadra.number_3_politico,
    forms.ModelChoiceField,
    widget=autocomplete.ModelSelect2(url='politico-autocomplete')
)
djhacker.formfield(
    Squadra.number_4_politico,
    forms.ModelChoiceField,
    widget=autocomplete.ModelSelect2(url='politico-autocomplete')
)
djhacker.formfield(
    Squadra.number_5_politico,
    forms.ModelChoiceField,
    widget=autocomplete.ModelSelect2(url='politico-autocomplete')
)
djhacker.formfield(
    Squadra.number_6_politico,
    forms.ModelChoiceField,
    widget=autocomplete.ModelSelect2(url='politico-autocomplete')
)
djhacker.formfield(
    Squadra.number_7_politico,
    forms.ModelChoiceField,
    widget=autocomplete.ModelSelect2(url='politico-autocomplete')
)
djhacker.formfield(
    Squadra.number_8_politico,
    forms.ModelChoiceField,
    widget=autocomplete.ModelSelect2(url='politico-autocomplete')
)
djhacker.formfield(
    Squadra.number_9_politico,
    forms.ModelChoiceField,
    widget=autocomplete.ModelSelect2(url='politico-autocomplete')
)
djhacker.formfield(
    Squadra.number_10_politico,
    forms.ModelChoiceField,
    widget=autocomplete.ModelSelect2(url='politico-autocomplete')
)
djhacker.formfield(
    Squadra.number_11_politico,
    forms.ModelChoiceField,
    widget=autocomplete.ModelSelect2(url='politico-autocomplete')
)
