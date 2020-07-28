from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from rest_framework.generics import ListAPIView
from django.contrib.auth import authenticate , login

from .models import Todo
from .serializers import TodoSerializer


#View to register an agent
@api_view(["POST"])
def register_agent(request):
    agent_id = request.data["agent_id"]
    password = request.data["password"]

    user = User()
    user.username = agent_id
    user.set_password(password)
    user.save()

    return Response(
        {
            "status":"account created",
            'status_code':status.HTTP_200_OK,
        }
    )

#View to login an agent
@api_view(["POST"])
def login_agent(request):
    agent_id = request.data["agent_id"]
    password = request.data["password"]

    user = authenticate(request , username=agent_id , password = password)

    if user is not None:
        # login(request , user)
        return Response(
            {
                "status":"success",
                "agent_id":agent_id,
                "status_code":status.HTTP_200_OK,
            }
        )
    else:
        return Response(
            {
                "status":"Failure",
                "status_code":status.HTTP_401_UNAUTHORIZED,
            }
        )

#View to create a todo post
@api_view(["POST"])
def create_post(request):
    agent_id = request.GET.get("agent" , "")

    try:
        user = User.objects.get(username = agent_id)
    except User.DoesNotExists:
        print("User does not exist")
    
    todo = Todo()
    todo.username = agent_id
    todo.todo_title = request.data["title"]
    todo.todo_description = request.data["description"]
    todo.category = request.data["category"]
    todo.due_date = request.data["due_date"]

    todo.save()

    return Response(
        {
            "status" : "Success",
            "status_code" : status.HTTP_200_OK,
        }
    )

#View to list down all todo posts
class TodoList(ListAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        print(self.request.GET.get("agent" , ""))
        query_set = Todo.objects.filter(username = self.request.GET.get("agent" , "")).order_by("-due_date")[::-1]
        print(query_set)
        return query_set
