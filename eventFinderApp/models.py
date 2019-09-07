from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_time = models.DateTimeField('start time and date')
    end_time = models.DateTimeField('end time and date')
    venue = models.CharField(max_length=200, null=True)
    category = models.ManyToManyField('Category')

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    # def __str__(self):
    #     return self.name