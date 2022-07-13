from rest_framework.test import APIRequestFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Todo


class TodoTests(APITestCase):
    def test_todo_list(self):

        # Creating a set of todos
        Todo.objects.create(
            title="Todo #1", body="-", deadline="2022-07-30")
        Todo.objects.create(
            title="Todo #2", body="-", deadline="2022-07-30")
        Todo.objects.create(
            title="Todo #3", body="-", deadline="2022-07-30")

        # Check amount of todos returned
        response = self.client.get(reverse('todo-list'))
        self.assertEqual(len(response.data), 3)


    def test_todo_details(self):

        # Creating a new todo
        Todo.objects.create(
            title="Look up", body="In the sky", deadline="2022-07-30")

        # Requesting todo to check all the fields
        response = self.client.get(reverse('todo-details', kwargs={'pk': 1}))
        self.assertEqual(response.data['title'], "Look up")
        self.assertEqual(response.data['body'], "In the sky")
        self.assertEqual(response.data['deadline'], "2022-07-30")
        self.assertEqual(response.data['is_completed'], False)

    def test_todo_create(self):

        # Post request to create a todo
        response = self.client.post(reverse('todo-create'), {
            "title": "Look up",
            "body": "In the sky",
            "deadline": "2022-07-30"
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), 1)

    def test_todo_complete(self):

        # Creating a new todo
        Todo.objects.create(
            title="Look up", body="In the sky", deadline="2022-07-30")

        # Make sure it's not completed
        todo = Todo.objects.get(id=1)
        todo.is_completed = False
        todo.save()

        # Requesting todo to check if it's incompleted
        response = self.client.get(reverse('todo-details', kwargs={'pk': 1}))
        self.assertEqual(response.data['is_completed'], False)

        # Post request to complete todo
        self.client.post(reverse('todo-complete', kwargs={'pk': 1}))

        # Requesting todo to check if it's completed
        response = self.client.get(reverse('todo-details', kwargs={'pk': 1}))
        self.assertEqual(response.data['is_completed'], True)

    def test_todo_delete(self):
        
        # Creating a new todo
        Todo.objects.create(
            title="Look up", body="In the sky", deadline="2022-07-30")

        # Check amount of todos
        response = self.client.get(reverse('todo-list'))
        self.assertEqual(len(response.data), 1)

        # Remove todo
        response = self.client.delete(reverse('todo-delete', kwargs={'pk': 1}))

        # Check amount of todos to be 0
        response = self.client.get(reverse('todo-list'))
        self.assertEqual(len(response.data), 0)
