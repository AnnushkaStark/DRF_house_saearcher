from django.db import models

# Create your models here.
class Houses(models.Model):
    '''Модель для хранения запросов и их статусов'''
    width = models.DecimalField(max_digits=10,decimal_places=7)
    lenght = models.DecimalField(max_digits=10,decimal_places=7)
    cad_number = models.IntegerField()
    status = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.width, self.lenght, self.cad_number, self.status, self.date
