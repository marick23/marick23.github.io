from django.db import models

# Create your models here.
class Infor(models.Model):
    name = models.TextField()
    memberid = models.TextField()
    pw = models.TextField()
    phonenumber = models.TextField()
    email = models.TextField()
    address = models.TextField()