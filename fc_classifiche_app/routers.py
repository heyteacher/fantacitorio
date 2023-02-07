from django.conf import settings

class ClassificheRouter:
    route_app_label = 'fc_classifiche_app'
    route_db = 'db_classifiche' if 'db_classifiche' in settings.DATABASES else 'default'
    
    def db_for_read(self, model, **hints):
        if model._meta.app_label == self.route_app_label:
            return self.route_db
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == self.route_app_label:
            return self.route_db
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == self.route_app_label:
            return db == self.route_db
        return None