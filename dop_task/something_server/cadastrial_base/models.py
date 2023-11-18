from django.db import models

# Create your models here.
class CadastrialBase(models.Model):

    '''Модель для хранения широты долготы и кадастрового номера'''

    latitude = models.DecimalField(max_digits=10,decimal_places=7)  #Широта
    longitude = models.DecimalField(max_digits=10,decimal_places=7)  #Долгота
    cad_number = models.IntegerField()                              #Кадастровый номе                  
                  

    def __str__(self):
        return f'{self.latitude}, {self.longitude}, {self.cad_number}'
