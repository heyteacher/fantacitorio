"""fc_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import RedirectView
from fc_classifiche_app.views import ClassificaGeneraleListView, ClassificaPerLegaListView, \
    ClassificaPoliticoListView, SquadraPuntiListView, PunteggioPuntataListView, RefreshClassificheView
from fc_classifiche_app.sitemaps import ClassificaGeneraleSitemap, ClassificaPoliticoSitemap, PunteggioPuntataPoliticoSitemap
from fc_gestione_app.views import SquadraUpdateView, SquadraCreateView, SquadraDetailView, PoliticoAutocompleteView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',RedirectView.as_view(pattern_name='classifica_generale'), name='home'),
    path('classifica_generale', ClassificaGeneraleListView.as_view(), name='classifica_generale'),
    path('classifica_per_lega', ClassificaPerLegaListView.as_view(), name='classifica_per_lega'),
    path('classifica_politico', ClassificaPoliticoListView.as_view(), name='classifica_politico'),
    path('punteggio_puntata', PunteggioPuntataListView.as_view(), name='punteggio_puntata'),
    path('squadra_punti/<squadra_id>', SquadraPuntiListView.as_view(), name='squadra_punti'),
    path('refresh_classifiche', RefreshClassificheView.as_view(), name='refresh_classifiche'),
    path('politico-autocomplete/', PoliticoAutocompleteView.as_view(), name='politico-autocomplete'),
    path('sitemap.xml', 
        sitemap, 
        {
            "sitemaps": {
                'classifica_generale': ClassificaGeneraleSitemap(), 
                'classifica_politico': ClassificaPoliticoSitemap(), 
                'punteggio_puntata': PunteggioPuntataPoliticoSitemap()
            }
        }, 
        name="django.contrib.sitemaps.views.sitemap"
    )
] 

if settings.ALLAUTH_ENABLED:
    urlpatterns += [
        path('accounts/', include('allauth.urls')),
        path('squadra/add/', SquadraCreateView.as_view(), name='squadra-add'),
        path('squadra/edit/', SquadraUpdateView.as_view(), name='squadra-update'),
        path('squadra/detail/', SquadraDetailView.as_view(), name='squadra-detail'),
    ]

# DEBUG TOOLBAR
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]