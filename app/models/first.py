from django.db import models


class First(models.Model):
    field_one = models.CharField(max_length=30)
    field_two = models.CharField(max_length=30)
    second = models.OneToOneField('Second', blank=True, null=True, on_delete=models.PROTECT)