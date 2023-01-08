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
from django.urls import path,reverse_lazy
#from django.views.generic.base import RedirectView
#from django.contrib.auth import views as auth_views
from fc_classifiche_app.views import ClassificaGeneraleListView, ClassificaPerLegaListView, ClassificaPoliticoListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ClassificaGeneraleListView.as_view()),
    path('classifica_per_lega', ClassificaPerLegaListView.as_view()),
    path('classifica_politico', ClassificaPoliticoListView.as_view()),

#    path(
#        'admin/password_reset/',
#        auth_views.PasswordResetView.as_view(),
#        name='admin_password_reset',
#    ),
#    path(
#        'admin/password_reset/done/',
#        auth_views.PasswordResetDoneView.as_view(),
#        name='password_reset_done',
#    ),
#    path(
#        'reset/<uidb64>/<token>/',
#        auth_views.PasswordResetConfirmView.as_view(),
#        name='password_reset_confirm',
#    ),
#    path(
#        'reset/done/',
#        auth_views.PasswordResetCompleteView.as_view(),
#        name='password_reset_complete',
#    ),
 #   path('', RedirectView.as_view(url=reverse_lazy('admin:index'))),
] 
