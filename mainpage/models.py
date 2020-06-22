from django.db import models
from myauth.models import User

class Deal(models.Model):
    title = models.CharField(max_length = 40, blank=False)
    more = models.CharField(max_length = 200, blank=True, default="Отсутствует")
    image = models.CharField(max_length = 150, blank=True, default="https://www.salonlfc.com/wp-content/uploads/2018/01/image-not-found-scaled-1150x647.png")
    address = models.CharField(max_length = 100, blank=True, default="Отсутствует")
    price = models.CharField(max_length=40, blank=True, default="Отсутствует")
    by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    

    