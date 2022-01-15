from django.db import models

# Create your models here.

class Sum(models.Model):
    number1  = models.IntegerField(null = False, blank = False)
    number2  = models.IntegerField(null = False, blank = False)
    answer  = models.IntegerField(null = True)

# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .tasks import calculate_sum
# import celery 

# @receiver(post_save, sender=Sum, dispatch_uid="calculate_answer")
# def user_sum_save(instance, signal, *args, **kwargs):
    # payload = {instance.number1,instance.number2,instance.pk}
    # print(payload)
    # payload = 'jkl'
    # celery.send_task('tasks.calculate_sum', (payload,), queue="sum_finder")
    # calculate_sum.delay(instance.number1,instance.number2,instance.pk)
    # print(instance.number1,instance.number2,instance.pk)
