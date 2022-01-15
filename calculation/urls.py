''' defines path to calculate sum '''
from django.urls import path
from . import views

urlpatterns = [
    path('<int:number_1>/<int:number_2>/', views.CalculateAPIView.as_view(),
    name='CalculateAPIView'),
]
