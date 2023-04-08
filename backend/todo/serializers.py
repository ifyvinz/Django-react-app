from rest_framework import serializers
from .models import User, Todo, Completed

class TodoSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    title = serializers.StringRelatedField()
    description = serializers.StringRelatedField()
    timestamp = serializers.DateTimeField(format="%I:%M %p, %a %d %B %Y")
    class Meta:
        model = Todo
        fields = ['id', 'author', 'title', 'description', 'completed', 'timestamp']
    

class UserSerializer(serializers.ModelSerializer):
    
    timestamp = serializers.DateTimeField(format="%I:%M %p, %a %d %B %Y")
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'photo']

class CompletedSerializer(serializers.ModelSerializer):
   
    completed_by = serializers.StringRelatedField()
    completed_task = serializers.StringRelatedField()
    timestamp = serializers.DateTimeField(format="%I:%M %p, %a %d %B %Y")
    class Meta:
        model = Completed
        fields = ['id', 'completed_by', 'completed_task', 'timestamp']