''' define path to get answer'''
from django.urls import path
from . import views

urlpatterns = [
    path('<int:identifier>/', views.GetAnswerAPIView.as_view(), name='GetAnswerAPIView'),
]
