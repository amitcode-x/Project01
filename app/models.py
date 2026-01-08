from django.db import models

# Create your models here.


class Topic(models.Model):
    topic_name = models.CharField(max_length=100, unique=True)
    desc = models.CharField(max_length=100, null= True)
    created_at = models.DateTimeField(null=True)


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField()
    s_name= models.CharField(max_length=100, null= True)
    sort = models.IntegerField(null=True)


class AccessRecord(models.Model):
    Webpages = models.ForeignKey(Webpage, on_delete=models.CASCADE)
