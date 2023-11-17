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


class QueryView(APIView):
    '''Получение запроса (широта долгота кадастровый номер)'''
    def get(self,request):
        data = {'latitude':48.857896, 'longitude': 2.295258, 'cad_number': 10989375648, 'status':True} # тестовые переданные параметры широта долгота кадастровый номер
        serializer = HousesSerializer(data=data)    #Проверяем валиднось сериалайзера
        if serializer.is_valid():    #Если сериалайзер валидный 
            serializer.save()         #Сохраняем запрос в базе данных 
            return Response(serializer.data,status=status.HTTP_201_CREATED)   # Статус 201 запрос сохранен
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   # Статус Ошибка валидации


class ResultView(APIView):
    def get(self):
        try:
            url = 'http://something-server-url/'
            data = {'latitude':48.857896, 'longitude': 2.295258, 'cad_number': 10989375648, 'status':True}
            response = requests.get(url,data=data)
            if response.status_code == 200:
                serializer = HousesSerializer(data=data)    #Проверяем валиднось сериалайзера
                if serializer.is_valid():  #Если сериалайзер валидный   
                    serializer.save()         #Сохраняем ответ на запрос в базе данных в базе данных 
                    return Response(serializer.data,status=status.HTTP_201_CREATED)   # Статус 201 запрос сохранен
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   # Статус Ошибка валидации
            return Response({'message': 'Error connection to external server'})  # Если статус не 200 вернем это сообщениe
        except requests.exceptions.Timeout:                    # Обработка исключени timeout
            return Response({'message': 'Request timed out'})
        except  requests.exceptions.ConnectionError:            # Connection error
            return Response({'message': 'Connection Error'})
        



class HistoryViiew(generics.ListAPIView):
    '''вывод истории и статуса запросов '''
    queryset = Houses.objects.all()     # обращаемся к модели Houses
    serializer_class = HousesSerializer    # Выводим все через  сериалайзер