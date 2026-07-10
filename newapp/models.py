from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    roll=models.IntegerField(primary_key=True)
    age=models.IntegerField()
    fathers_name=models.CharField(max_length=30)
    def __str__(self):
        return f"{self.name} - {self.roll}"
