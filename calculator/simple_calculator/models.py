from django.db import models
from django.db.models.fields import CharField, DateTimeField


class Calculation(models.Model):
    calculation = models.CharField(max_length=200, null=False)

    def __str__(self):
        return str(self.calculation)

