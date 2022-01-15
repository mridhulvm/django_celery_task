''' for class based views '''
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from calculation.models import Sum

import logging
logger = logging.getLogger(__name__)

class GetAnswerAPIView(APIView):
    ''' accept two integer number via url parameters '''

    def get(self, request, identifier = None):
        ''' check database using sum table id and returns corresponding status codes '''
        # logger.warning(identifier)
        try:
            sum_instance = Sum.objects.get(id = identifier)
            # logger.warning('not in except')
            if sum_instance.answer is None:
                data = 'Please wait.'
                return Response(data,status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_200_OK)

        except Sum.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
