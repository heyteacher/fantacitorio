from django.db import connection
from django.core.management.base import BaseCommand
from fc_classifiche_app.models import ClassificaGenerale, PunteggioPuntata
from fc_gestione_app.models import Squadra, Punteggio
from django.core.mail import send_mail
import os

class Command(BaseCommand):
    help = 'Refresh PostgreSQL materialized views'

    def handle(self, *args, **options):
        queries = [
            'REFRESH MATERIALIZED VIEW punteggio_puntata',
            'REFRESH MATERIALIZED VIEW squadra_punti',
            'REFRESH MATERIALIZED VIEW classifica_per_lega',
            'REFRESH MATERIALIZED VIEW classifica_politico',
            'REFRESH MATERIALIZED VIEW classifica_generale',
        ]
        self.stdout.write(self.style.SUCCESS('Starting Refresh Postgres materialized views'))
        try:
                punteggioPuntataCount = PunteggioPuntata.objects.count()
                classificaGeneraleCount = ClassificaGenerale.objects.count()
                squadraCount = Squadra.objects.count()
                punteggioCount = Punteggio.objects.count()
        except:
                punteggioPuntataCount = 0
                classificaGeneraleCount = 0
                squadraCount = 0
                punteggioCount = 0

        self.stdout.write(self.style.SUCCESS('Count before: ClassificaGenerale %s, Squadre %s, PunteggiPuntata %s, Punteggi %s' % (
                classificaGeneraleCount,
                squadraCount,
                punteggioPuntataCount,
                punteggioCount
                )
        ))
        with connection.cursor() as cursor:
            for query in queries:
                try:
                        self.stdout.write(self.style.NOTICE('EXECUTE: %s' % query))
                        cursor.execute(query)
                except Exception as e:
                        self.stderr.write(self.style.ERROR('ERROR EXECUTING: %s error %s' % (query,e)))
                        
        self.stdout.write(self.style.SUCCESS('Count after: ClassificaGenerale %s, Squadre %s, PunteggiPuntata %s, Punteggi %s' % (
                classificaGeneraleCount,
                squadraCount,
                punteggioPuntataCount,
                punteggioCount
                )
        ))
        self.stdout.write(self.style.SUCCESS('Refresh Done'))
        send_mail(
                '[%s] Refresh sqlite classifiche' % (os.environ.get('STAGE'),),
                'ClassificaGenerale:\t%s\nSquadre:\t\t%s\nPunteggiPuntata:\t%s\nPunteggi:\t\t%s' % (
                        classificaGeneraleCount,
                        squadraCount,
                        punteggioPuntataCount,
                        punteggioCount
                ),
                os.environ.get('DEFAULT_FROM_EMAIL'),
                [os.environ.get('EMAIL_MANAGER_EMAIL')]
        )
