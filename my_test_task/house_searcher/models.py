from django.db import models

# Create your models here.
class Houses(models.Model):
    '''Модель для хранения запросов и их статусов'''
    latitude = models.DecimalField(max_digits=10,decimal_places=7)  #Широта
    longitude = models.DecimalField(max_digits=10,decimal_places=7)  #Долгота
    cad_number = models.IntegerField()                              #Кадастровый номер
    status = models.BooleanField(null=True,blank=True)                      #Ответ сервера
    date = models.DateTimeField(auto_now_add=True)                   #Дата запроса

    def __str__(self):
        return f'{self.latitude}, {self.longitude}, {self.cad_number}, {self.status}, {self.date}'
