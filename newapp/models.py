from django.db import models

class data1(models.Model):
    petname=models.CharField(max_length=255)
    price=models.CharField(max_length=255)

