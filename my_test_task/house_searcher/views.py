#from django.shortcuts import render_to_response
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Houses
import requests
from rest_framework.views import APIView
from .serializers import HousesSerializer



# Create your views here.
class PingView(APIView):
    '''Проверка запуcка серверa'''
    def get(self,request):
        try:
            response = requests.get('http://something-server-url/ping',timeout=60) # Отправляем запрос к стороннему серверу
            if response.status_code == 200:            
                return Response({'message':'External server is running'})   # Если статус запроса 200 и уложлись в 60 секунд  сервер запущен
            else:
                return Response({'message':'Exteral server not running'})    # В случае другого статуса запроса сервер не запущен
        except requests.exceptions.Timeout:                                
            return Response({'message': 'Request timed out'})              # Обработка исключения превышен таймаут запроса 60 секунд
        except requests.exceptions.RequestException:
            return Response({'message': 'Error connection to external server'})  # Обработка исключения ошибка соединения


class QueryView(generics.CreateAPIView):
    '''Получение запроса (широта долгота кадастровый номер)'''
    pass 

class ResultView(APIView):
    pass


class HistoryViiew(generics.ListAPIView):
    '''вывод истории и статуса запросов '''
    queryset = Houses.objects.all()     # обращаемся к модели Houses
    serializer_class = HousesSerializer    # Выводим все через  сериалайзер