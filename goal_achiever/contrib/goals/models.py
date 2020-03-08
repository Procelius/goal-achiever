from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name


class Task(Item):
    pass


class Restriction(Item):
    pass


class Goal(Item):
    tasks = models.ManyToManyField(Task, blank=True)
    restrictions = models.ManyToManyField(Restriction, blank=True)
