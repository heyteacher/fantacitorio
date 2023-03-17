from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import Squadra

@receiver(user_logged_in)
def post_login(sender, user, request, **kwargs):
    squadra = Squadra.objects.filter(utente=user).first()
    if squadra is not None:
        request.session['squadra_id'] =squadra.id
        print('post_login', user.username, 'squadra_id', squadra.id)
    else:
        print('post_login', user.username, 'no squadra_id')

