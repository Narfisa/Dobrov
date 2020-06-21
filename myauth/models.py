from django.db import models

class User(models.Model):
    login = models.CharField(max_length = 20, blank=False, default="")
    email = models.CharField(max_length = 40, blank=False, default="")
    password = models.CharField(max_length=30, blank=False, default="")
    phoneNumber = models.CharField(max_length=11, blank=True)
    firstName = models.CharField(max_length=20, blank=True)
    lastName = models.CharField(max_length=20, blank=True)
    birthday = models.DateField(blank=True, null=True)

    