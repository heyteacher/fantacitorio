from django.conf import settings

def fc_settings(request):
    return {
        'ALLAUTH_ENABLED': settings.ALLAUTH_ENABLED,
    }