from django.db import connection
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Refresh Postgres materialized views'

    def handle(self, *args, **options):
        queries = ['call public.refresh_mat_views()']
        self.stdout.write(self.style.SUCCESS('Starting Refresh Postgres materialized views'))
        with connection.cursor() as cursor:
            for query in queries:
                self.stdout.write(self.style.NOTICE('EXECUTE: %s' % query))
                cursor.execute(query)
        self.stdout.write(self.style.SUCCESS('Refresh Done'))