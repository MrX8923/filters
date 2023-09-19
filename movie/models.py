from django.db import models


class MovieModel(models.Model):
    title = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    year = models.CharField(max_length=40)


