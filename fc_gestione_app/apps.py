from django.apps import AppConfig


class FcGestioneAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fc_gestione_app'
    verbose_name = 'Gestione'

    def ready(self):
        import fc_gestione_app.signals

