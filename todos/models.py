from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=120)
    body = models.CharField(max_length=250)
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
