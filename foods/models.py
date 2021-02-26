from django.db import models

# Create your models here.
class Data(models.Model):

    def __str__(self):
        return self.food_desc

    food_name=models.CharField(max_length=100)
    food_desc=models.CharField(max_length=200)
    food_price=models.IntegerField()