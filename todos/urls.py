from django.urls import path
from .views import ListTodo, DetailTodo, CreateTodo, DeleteTodo, CompleteTodo


urlpatterns = [
    path('todos', ListTodo.as_view(), name='todo-list'),
    path('todos/<int:pk>', DetailTodo.as_view(), name='todo-details'),
    path('todos/<int:pk>/delete', DeleteTodo.as_view(), name='todo-delete'),
    path('todos/<int:pk>/complete', CompleteTodo.as_view(), name='todo-complete'),
    path('todos/create', CreateTodo.as_view(), name='todo-create')
]
