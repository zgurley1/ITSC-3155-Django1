from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    #setting null to true means that the field is allowed to be blank, allowing for updating later
    description = models.TextField(null=True, blank=True)
    #participants =
    #Everytime the save method is called it saves a timestamp
    updated = models.DateTimeField(auto_now=True)
    #auto now add only takes the timestamp when the initial instance is created
    created = models.DateField(auto_now_add=True)


    class Meta:
        #the dash means the newest items are first
        ordering = ['-updated', '-created']

    def __str__(self):
        return str(self.name)
    

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #When the parent is deleted, delete all the messages in the room
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]