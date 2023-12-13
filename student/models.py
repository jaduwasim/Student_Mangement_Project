# students/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Class(models.Model):
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return self.class_name

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=False)  # Inactive by default
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username
