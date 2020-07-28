from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Todo(models.Model):
    # username = models.ForeignKey(to=User , on_delete=models.CASCADE)
    username = models.CharField(max_length=10)
    todo_title = models.CharField(max_length = 256)
    todo_description = models.CharField(max_length = 512)
    category = models.CharField(max_length=256)
    due_date = models.DateField()
