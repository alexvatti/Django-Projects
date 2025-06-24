
# Create your models here.
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    course = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.roll_number} - {self.course}"