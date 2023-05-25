
from django.contrib.sitemaps import Sitemap
from .models import SquadraPunti

class ClassificaGeneraleSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1.0
    location = '/'
    protocol = 'https'

    def items(self):
        return SquadraPunti.objects.all()[:1]

    def lastmod(self, obj):
        return obj.puntata_data

class ClassificaPoliticoSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5
    location = '/classifica_politico'
    protocol = 'https'

    def items(self):
        return SquadraPunti.objects.all()[:1]

    def lastmod(self, obj):
        return obj.puntata_data

class PunteggioPuntataPoliticoSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5
    location = '/punteggio_puntata'
    protocol = 'https'

    def items(self):
       return SquadraPunti.objects.all()[:1]

    def lastmod(self, obj):
        return obj.puntata_data

