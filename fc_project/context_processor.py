from fc_project import settings

def fc_settings(request):
    return {
        'ALLAUTH_ENABLED': settings.ALLAUTH_ENABLED,
    }