'''for sleeping 10 seconds '''
import time
''' celery module for setting up tasks'''
from celery import shared_task
''' logger module'''
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)
from .models import Sum

@shared_task
def calculate_sum(number_1,number_2,unique_identifier):
    ''' background process of calculatin answer'''
    time.sleep(10)
    print(number_1,number_2,unique_identifier)
    answer = number_1 + number_2
    add_answer(answer,unique_identifier)

def add_answer(answer,unique_identifier):
    ''' updates answer field in database on getting answer from celery tasks'''
    try:
        sum_instance = Sum.objects.get(id=unique_identifier)
        sum_instance.answer = answer
        sum_instance.save()
    except Sum.DoesNotExist:
        pass
