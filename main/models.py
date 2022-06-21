from django.db import models
model = models.Model



class Student(model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.BigIntegerField()
    address = models.CharField(max_length=255)
    studyed = models.CharField(max_length=255)
    job = models.CharField(max_length=255)

    def __str__(self):
        return self.name

        