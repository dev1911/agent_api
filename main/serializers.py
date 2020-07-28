from rest_framework import serializers
from .models import Todo

# class AgentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Agent
#         fields = ["agent_id" , "password"]

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["username" , "todo_title" , "todo_description" , "category" , "due_date"]