from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=350)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)