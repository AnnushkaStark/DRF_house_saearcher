from django.urls import path
from .views import QueryView, ResultView,HistoryViiew,PingView

# url пути приложения

urlpatterns = [path('ping/',PingView.as_view(), name='ping'),   # Пинг - Проверка акивности сервера
               path('query/',QueryView.as_view(), name='query'),      # query - Отправка запроса 
               path('result/', ResultView.as_view(), name='result'),    #  result - получение ответа от сервера (True/False)
               path('history/',HistoryViiew.as_view(), name='history'),] # history - просмотр истории запросов