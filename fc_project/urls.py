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
from django.contrib.auth.decorators import login_required
from fc_classifiche_app.views import ClassificaGeneraleListView, ClassificaPerLegaListView, ClassificaPoliticoListView, SquadraPuntiListView

admin.site.login = login_required(admin.site.login)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', ClassificaGeneraleListView.as_view(), name='home'),
    path('classifica_per_lega', ClassificaPerLegaListView.as_view()),
    path('classifica_politico', ClassificaPoliticoListView.as_view()),
    path('classifica_politico', ClassificaPoliticoListView.as_view()),
    path('squadra_punti/<squadra_id>', SquadraPuntiListView.as_view(), name='squadra_punti'),
  ] 
