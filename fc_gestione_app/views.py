from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from dal import autocomplete
from .models import Squadra, Politico
import djhacker 
from django import forms
from django_tables2 import SingleTableView

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

class SquadraCreateView(CreateView):
    model = Squadra
    fields = fields

class SquadraUpdateView(UpdateView):
    model = Squadra
    fields = fields

class SquadraDetailView(DetailView):
    model = Squadra
    template_name = 'fc_gestione_app/dettaglio_squadra.html'

class PoliticoAutocompleteView(autocomplete.Select2QuerySetView):
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
