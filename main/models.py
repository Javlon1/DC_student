from distutils.command.upload import upload
from django.db import models
model = models.Model


class Info(models.Model):
    logo = models.ImageField(upload_to='logo/')
    img = models.ImageField(upload_to='img/')


class Student(model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.BigIntegerField()
    address = models.CharField(max_length=255)
    studyed = models.CharField(max_length=255)
    job = models.CharField(max_length=255)

    def __str__(self):
        return self.name