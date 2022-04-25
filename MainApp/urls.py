from django.urls import path

from . import views

app_name = "MainApp"

urlpatterns = [
    path('', views.index, name='index'), #'' auto refers to home page address
    path('topics', views.topics, name='topics'), #url/topics
]
