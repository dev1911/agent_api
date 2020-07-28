from django.urls import path
from .views import register_agent , login_agent , create_post , TodoList
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('agent/' , csrf_exempt(register_agent) , name="register"),
    path('agent/auth/' , csrf_exempt(login_agent) , name="login"),
    path('sites/' , csrf_exempt(create_post) , name="create_post"),
    path('sites/list/' , csrf_exempt(TodoList.as_view()) , name="list_post"),    
]