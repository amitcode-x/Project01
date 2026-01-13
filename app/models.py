from django.db import models

# Create your models here.


class Topic(models.Model):
    topic_name = models.CharField(max_length=100, unique=True)
    # desc = models.CharField(max_length=100, null= True)
    
    
    def __str__(self):
        return self.topic_name
    

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField()
    s_name= models.CharField(max_length=100, null= True)
    sort = models.IntegerField(null=True)
    
    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE, null= True)
    author = models.CharField(max_length=100, null= True)
    date = models.DateField()
    
