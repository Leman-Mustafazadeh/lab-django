from django.db import models

# Create your models here.

class Person(models.Model):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_pics/')

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
