from django.db import models

# Create your models here.

class Tasks(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
  
    def __str__(self):
        return str(self.id)