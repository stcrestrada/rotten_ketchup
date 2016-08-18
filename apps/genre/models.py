from __future__ import absolute_import

from django.db import models

from base.models import BaseModel


class Genre(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
