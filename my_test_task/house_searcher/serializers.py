from rest_framework import serializers
from .models import Houses

class HousesSerializer(serializers.ModelSerializer):
    '''Сериализация истории запросов из модели Houses'''
    class Meta:
        model = Houses      # Из модели Houses
        fields = '__all__'   # выыодим всю историю запросов (дата запроса, долгота, широта, кадастровый номер, статус)
       