from django.urls import path

from . import views

app_name = "MainApp"

urlpatterns = [
    path('', views.index, name='index'), #'' auto refers to home page address
    path('topics', views.topics, name='topics'), #url/topics]
    path('topics/<int:topic_id>/',views.topic, name='topic'), #url gets id added to it to go to differnt page
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
