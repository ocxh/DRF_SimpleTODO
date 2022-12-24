from django.db import models
from django.core.validators import MinLengthValidator

class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=15)
    description = models.TextField(blank=True)
    time = models.CharField(default="20230101",max_length=8,  validators=[MinLengthValidator(8)])
    done = models.BooleanField(default=False)