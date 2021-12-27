from django.db import models


class UserRegistration(models.Model):
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class meta:
        db_table = "appusers"