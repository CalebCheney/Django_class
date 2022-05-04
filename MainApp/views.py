from django.shortcuts import render , redirect

from .forms import TopicForm, EntryForm
from .models import Topic, Entry #adding topics needs to be imported
from django.contrib.auth.decorators import login_required
from django.http import Http404


# Create your views here.

def index(request):
    return render(request, 'MainApp/index.html')

@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('-date_added')


    context = {'topics':topics} #key value is what is used in html template, value is what you use in the view file

    return render(request, 'MainApp/topics.html', context)

@login_required
def topic(request, topic_id): #on exam topic_id has to be consistant with urls.py mainapp file
    topic = Topic.objects.get(id=topic_id)

    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added') #decending order

    context = {'topic':topic,'entries':entries} #key and value

    return render(request, 'MainApp/topic.html', context) #context is a dictionary object ! ON FINAL

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm #loads empty form
    else: 
        form = TopicForm(data=request.POST)

        if form.is_valid():
            new_topic = form.save(commit=False) 
            new_topic.owner = request.user
            new_topic.save()

            return redirect('MainApp:topics')
    context = {'form':form}
    return render(request, 'MainApp/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id) #creates instance 'topic' from models 'Topic'

    if topic.owner != request.user:
        raise Http404    
    
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic 
            new_entry.save()
            return redirect('MainApp:topic',topic_id=topic_id)

    context = {'form':form, 'topic':topic}
    return render(request, 'MainApp/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry) #brings in old entry so that we can edit it GET INSTANCE
    else:
        form = EntryForm(instance=entry, data=request.POST) #POST INSTANCE

        if form.is_valid():
            form.save()
            return redirect('MainApp:topic',topic_id=topic.id)

    context = {'form':form, 'topic':topic, 'entry':entry} 
    return render(request, 'MainApp/edit_entry.html', context)