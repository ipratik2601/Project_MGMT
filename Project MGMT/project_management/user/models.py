from email.policy import default
from django.db import models
from generic.models import *
from django.contrib.auth.models import AbstractUser


# Create your models here.
ROLE_CHOICE = (
    ('Admin', 'Admin'),
    ('Project-Manager' , 'Project-Manager'),
    ('Developer', 'Developer')
)

class  Role(BaseField):
    role_name = models.CharField(max_length=50,choices = ROLE_CHOICE)
 
    def __str__(self):
        return self.role_name

    class Meta():
        db_table = 'role'
    


class User(BaseField,AbstractUser):
    username = models.CharField(max_length=99,unique=True)
    profile_pic = models.ImageField(upload_to = 'profile_pic/',default="profile_pic/p1.jpg")
    email = models.EmailField(('email address'),max_length=150, unique=True)
    password = models.CharField(max_length=99)
    role = models.ForeignKey(Role,on_delete=models.CASCADE) 
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'User'
        db_table = 'user'

    def __str__(self):
        return self.username

    @property
    def imageURL(self):
        try:
            url = self.profile_pic.url
        except:
            url = ''
        return url