from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializer import TodoSerializer
from .models import Todo

# Create your views here.
class TodoView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()