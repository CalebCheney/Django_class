from django.shortcuts import render , redirect

from .forms import TopicForm
from .models import Topic #adding topics needs to be imported

# Create your views here.

def index(request):
    return render(request, 'MainApp/index.html')

def topics(request):
    topics = Topic.objects.all()


    context = {'topics':topics} #key value is what is used in html template, value is what you use in the view file

    return render(request, 'MainApp/topics.html', context)

def topic(request, topic_id): #on exam topic_id has to be consistant with urls.py mainapp file
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added') #decending order

    context = {'topic':topic,'entries':entries} #key and value

    return render(request, 'MainApp/topic.html', context) #context is a dictionary object ! ON FINAL

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm #loads empty form
    else: 
        form = TopicForm(data=request.POST)

        if form.is_valid():
            new_topic = form.save()

            return redirect('MainApp:topics')
    context = {'form':form}
    return render(request, 'MainApp/new_topic.html', context)




