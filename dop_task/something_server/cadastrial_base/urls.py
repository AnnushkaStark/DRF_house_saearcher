from django.urls import path
from .views import CadastreApiView, FoundApiView


urlpatterns = [
    path('cadasrtre/',CadastreApiView.as_view(), name = 'cadastre'), # вывод всех значнеий из бд
    path('found/',FoundApiView.as_view(), name= 'found') #Поиск по переданному запросу
    ]