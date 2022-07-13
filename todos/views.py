from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import TodoSerializer, TodoCreateSerializer
from .models import Todo

class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class CreateTodo(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoCreateSerializer


class DeleteTodo(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class CompleteTodo(APIView):
    def post(self, request, pk):
        todo = Todo.objects.get(pk=pk)
        todo.is_completed = True
        todo.save()
        return Response({"Success": f"Task '{todo.title}' is now completed"})

