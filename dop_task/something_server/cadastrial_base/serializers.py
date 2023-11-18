from rest_framework import serializers
from .models import CadastrialBase

class CadastreSerializer(serializers.ModelSerializer):
    '''Сериалайзер для получения занчений из базы данных'''
    class Meta:
        model = CadastrialBase
        fields = '__all__'