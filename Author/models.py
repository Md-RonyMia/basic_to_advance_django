from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=20)
    bio=models.CharField(max_length=40)
    phone=models.CharField(max_length=11)
    def __str__(self):
        return f"Author Name : {self.name} "
