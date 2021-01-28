from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    
    def __str__(self):
        return self.title

  
