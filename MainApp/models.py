from django.db import models

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True) #auto adds date and time 


    def __str__(self): #defines what to print
        return self.text #text is what we defined + '-' + str(self.date_added) to add to return value

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'entries' #over rides addind s to 'entrys'


    #shows the discription for the first 50 characters then ...
    def __str__(self): #defines what to print
        return f"{self.text[:50]}..." #text is what we defined 

    
