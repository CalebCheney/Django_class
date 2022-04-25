from django.shortcuts import render
from .models import Topic #adding topics needs to be imported

# Create your views here.

def index(request):
    return render(request, 'MainApp/index.html')

def topics(request):
    topics = Topic.objects.all()


    context = {'topics':topics} #key value is what is used in html template, value is what you use in the view file

    return render(request, 'MainApp/topics.html', context)
