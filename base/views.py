''' Function based views modules '''
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def base_testing(request):
    ''' Testing API and returns testing string '''    
    data = "Hi from test API"
    return Response(data, status=status.HTTP_200_OK)
