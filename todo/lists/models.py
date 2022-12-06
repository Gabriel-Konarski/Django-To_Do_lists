from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class List(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Item(models.Model):
    lists = models.ForeignKey(List, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False)
    complete = models.BooleanField()

    def __str__(self):
        return self.name