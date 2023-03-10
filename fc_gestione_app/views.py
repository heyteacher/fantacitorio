from django.views.generic.edit import CreateView, DeleteView, UpdateView
from dal import autocomplete
from .models import Squadra, Politico
import djhacker  # don't forget to pip install djhacker
from django import forms

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