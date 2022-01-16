''' for class based views '''
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
''' logger'''
import logging
logger = logging.getLogger(__name__)
''' model to store data '''
from .models import Sum
''' imported celery task '''
from .tasks import calculate_sum

class CalculateAPIView(APIView):
    ''' accept two integer number via url parameters '''

    def get(self, request, number_1 = None, number_2 = None):
        ''' store data in database and queue, then return the database entry id '''
        logger.info(number_1,number_2)
        if len(str(number_1)) > 19 or len(str(number_2)) > 19:
            #As per sqlite3 database limitation in int
            return Response(status=status.HTTP_400_BAD_REQUEST)
        sum_instance = Sum.objects.create(number1=number_1, number2=number_2)
        data = sum_instance.pk
        calculate_sum.delay(sum_instance.number1,sum_instance.number2,sum_instance.pk)
        #callint background task
        return Response(data,status=status.HTTP_200_OK)
