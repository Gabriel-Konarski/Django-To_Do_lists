from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

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