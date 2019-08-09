from django.db import models


class account(models.Model):
    user = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=15)


class D_O2(models.Model):
    Year = models.IntegerField()
    Province = models.CharField(max_length=15)
    Data = models.FloatField()