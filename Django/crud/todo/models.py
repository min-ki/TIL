from django.db import models


class Todo(models.Model):

    todo = models.CharField(max_length=100)  # 할일
    create_at = models.DateTimeField(auto_now=True)
