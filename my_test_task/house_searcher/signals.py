from .models import Houses
from django.db.models.signals import post_save
from django.dispatch import receiver
import requests


@receiver(post_save, sender=Houses)
def create_profile(sedner,instance: Houses, created, **kwargs):
    '''Сигнал который сохраняет статус запроса после того как запрос передан на сторонний сервер'''
    if created:
        try:
            url = 'http://something-server-url/'
            data = {'latitude':48.857896, 'longitude': 2.295258, 'cad_number': 10989375648,}
            response = requests.get(url,data=data)
            if response.status_code == 200 :
                instance.status = True
                instance.save()

        except requests.exceptions.Timeout:          # Обработка исключени timeout
            return {'message': 'Request timed out'}
        except  requests.exceptions.ConnectionError:  # Connection error
            return {'message': 'Connection Error'}
        