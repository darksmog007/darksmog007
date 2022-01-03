from django.db import models


class UserRegistration(models.Model):
    userid = models.CharField(max_length=500)
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    Phone = models.CharField(max_length=200 , blank=True)
    pincode = models.CharField(max_length=200, blank=True)
    Gender = models.CharField(max_length=200, blank=True)
    Martialsts = models.CharField(max_length=200, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class meta:
        db_table = "appusers"