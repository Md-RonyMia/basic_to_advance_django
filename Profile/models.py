from django.db import models
from Author.models import Author

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=20)
    about=models.CharField(max_length=40)
    author=models.OneToOneField(Author,related_name='author',on_delete=models.CASCADE)
    def __str__(self):
        return f"Author Name : {self.name} "
