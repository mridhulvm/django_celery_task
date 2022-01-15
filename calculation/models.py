from django.db import models

# Create your models here.

class Sum(models.Model):
    number1  = models.IntegerField(null = False, blank = False)
    number2  = models.IntegerField(null = False, blank = False)
    answer  = models.IntegerField(null = True)
