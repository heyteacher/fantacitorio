from django.db import connection
from django.core.management.base import BaseCommand
from fc_classifiche_app.models import ClassificaGenerale

class Command(BaseCommand):
    help = 'Refresh Postgres materialized views'

    def handle(self, *args, **options):
        queries = ['call public.refresh_mat_views()']
        self.stdout.write(self.style.SUCCESS('Starting Refresh Postgres materialized views'))
        self.stdout.write(self.style.SUCCESS('ClassificaGenerale count before: %s' % ClassificaGenerale.objects.count()))
        with connection.cursor() as cursor:
            for query in queries:
                self.stdout.write(self.style.NOTICE('EXECUTE: %s' % query))
                cursor.execute(query)
        self.stdout.write(self.style.SUCCESS('ClassificaGenerale count after: %s' % ClassificaGenerale.objects.count()))
        self.stdout.write(self.style.SUCCESS('Refresh Done'))