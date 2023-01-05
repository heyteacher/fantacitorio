from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Truncate tables'

    def handle(self, *args, **options):
        queries = [
"""
delete from squadra
"""]
        self.stdout.write(self.style.SUCCESS('Starting truncate tables'))

        dbname = settings.DATABASES['default']['NAME']
        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        host = settings.DATABASES['default']['HOST']

        con = None
        con = connect(dbname='postgres', user=user, host=host, password=password)
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = con.cursor()
        for query in queries:
            self.stdout.write(self.style.NOTICE('EXECUTE: %s' % query))
            cur.execute(query)
        cur.close()
        con.close()

        self.stdout.write(self.style.SUCCESS('All Done'))