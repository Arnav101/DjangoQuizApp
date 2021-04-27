from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logoff', views.logoff, name="Logoff"),
    path('question', views.question, name="Question"),
]