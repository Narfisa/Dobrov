from django.db import models

class User(models.Model):
    login = models.CharField(max_length = 20, blank=False, default="")
    email = models.CharField(max_length = 40, blank=False, default="")
    image = models.CharField(max_length = 150, blank=False, default="https://www.salonlfc.com/wp-content/uploads/2018/01/image-not-found-scaled-1150x647.png")
    password = models.CharField(max_length=30, blank=False, default="")
    phoneNumber = models.CharField(max_length=11, blank=True)
    firstName = models.CharField(max_length=20, blank=True)
    lastName = models.CharField(max_length=20, blank=True)
    birthday = models.DateField(blank=True, null=True)
    