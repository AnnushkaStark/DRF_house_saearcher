from django.shortcuts import render
from rest_framework import generics, status
from .models import CadastrialBase
from .serializers import CadastreSerializer
from rest_framework.response import Response


# Create your views here.
class CadastreApiView(generics.ListAPIView):
    '''Предатсвление для получения всех данных из базы данных сайта'''
    queryset = CadastrialBase.objects.all() # чтобы проверить наличие запрашиваемого объекта в базе выбираем все значения
    serializer_class  = CadastreSerializer


class FoundApiView(generics.ListAPIView):
    '''Получение ответа True или False при запросе из нашего превого приложения '''
    def get(self,request):
        try: # тестовые значения которые принимает сервер
            data = {
                   'latitude': 77.03655,   #Широта 
                   'longitude':38.8976694,   # Долгота 
                    'cad_number': 5375398839   # кадастровый номер
                    }
            # Проверяме есть ли такое совпадение по широте долготе и кадастровому номеру в базе
            serializer_class  = CadastreSerializer
            if data in serializer_class:       # Если есть возвращаем status: True
                message = {'status':True}    
                return Response(message,status=status.HTTP_200_OK)
            message = {'status':False}                                  # Если нет возвращаем status:False
            return Response(message,status=status.HTTP_404_NOT_FOUND)
        except Exception:
            # Если нет возвращаем статус False
            message = {'status':False}                                # На всякий случай оработаем возможные исключения
            return Response(message,status=status.HTTP_404_NOT_FOUND)