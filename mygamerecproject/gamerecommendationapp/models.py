from django.db import models

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # Add other fields as needed

    def __str__(self):
        return self.title


class React(models.Model): 
    name = models.CharField(max_length=30) 
    detail = models.CharField(max_length=500)
