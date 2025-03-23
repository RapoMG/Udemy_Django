from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Main(models.Model):

    name = models.TextField()
    # about = models.TextField(default="-") # default ads string that will fill field when its created.
    about = models.TextField()

    # add name field for created objects
    def __str__(self):
        return self.name
