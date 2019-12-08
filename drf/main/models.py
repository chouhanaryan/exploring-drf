from django.db import models as models
from django.contrib.auth.models import AbstractUser

class Person(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    dob = models.DateField(auto_created=True)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class House(models.Model):
    loc = models.CharField(max_length=50, null=True)
    owner = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True)
    pin = models.IntegerField(unique=True)

    def __str__(self):
        return self.loc
    
class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    # phone = models.CharField(max_length=255)
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return (self.first_name + ' ' + self.last_name + ' / ' + self.email)