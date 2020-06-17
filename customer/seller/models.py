import json
import redis
from django.conf import settings
from django.db import models


class Vehicle(models.Model):
    name = models.CharField(
        max_length=64,
        help_text="",
    )
    wheels = models.IntegerField()
    brand = models.CharField(
        max_length=64,
        help_text="",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
