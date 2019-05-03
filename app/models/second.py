from django.db import models


class Second(models.Model):
    field_one = models.CharField(max_length=30)
    field_two = models.CharField(max_length=30)
