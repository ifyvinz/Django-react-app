from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    pass
    photo = models.ImageField(blank=True, null=True, upload_to='images/')
    

class Todo(models.Model):
    author =  models.ForeignKey(User, on_delete=models.CASCADE, related_name= "author")
    title = models.CharField(max_length=150)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.title} was posted on: {self.timestamp}"
    
class Completed(models.Model):
    completed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "completed_by")
    completed_task = models.OneToOneField(Todo, on_delete=models.CASCADE, related_name= "completed_task")
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.completed_by} {self.completed_task}, on: {self.timestamp}"
