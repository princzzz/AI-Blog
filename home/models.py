from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

#blog model
class Blog(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    is_approved = models.BooleanField(default=False)
    authorId=models.IntegerField(default=0)
    author=models.CharField(max_length=50)
    slug=models.CharField(max_length=200,unique=True)
    views=models.IntegerField(default=0)
    timeStamp=models.DateTimeField(blank=True)
    content=models.TextField()
    class Meta:
        ordering = ['-timeStamp',]
        unique_together = ["title", "slug"]
    def __str__(self):
        return self.title + " by " + self.author

#contact
class Contact(models.Model):
    sno= models.AutoField(primary_key=True)
    name= models.CharField(max_length=255)
    email= models.CharField(max_length=100)
    content= models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
          return "Message from " + self.name + ' - ' + self.email

#upcoming events
class PreEvent(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    is_approved = models.BooleanField(default=False)
    speaker=models.CharField(max_length=50)
    slug=models.CharField(max_length=200)
    timeStamp=models.DateTimeField(blank=True)
    content=models.TextField()
    class Meta:
        ordering = ['-timeStamp',]
    def __str__(self):
        return self.title + " by " + self.speaker

#list of all the events
class PostEvent(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    is_approved = models.BooleanField(default=False)
    speaker=models.CharField(max_length=50)
    slug=models.CharField(max_length=200,unique=True)
    views=models.IntegerField(default=0)
    timeStamp=models.DateTimeField(blank=True)
    content=models.TextField()
    class Meta:
        ordering = ['-timeStamp',]
        unique_together = ["title", "slug"]
    def __str__(self):
        return self.title + " by " + self.speaker

class Email(models.Model):
    address=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.address