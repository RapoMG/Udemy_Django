from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Main(models.Model):

    name = models.TextField()
    # about = models.TextField(default="-") # default ads string that will fill field when its created.
    about = models.TextField()

    # social media
    fb = models.TextField(default="value")
    tw = models.TextField(default="value")
    yt = models.TextField(default="value")



    # add name field for created objects in administration module
    def __str__(self):
        return self.name
