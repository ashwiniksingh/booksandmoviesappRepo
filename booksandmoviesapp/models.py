from django.db import models

# Create your models here.
class booksandmovies(models.Model):
    booksandmovies_name = models.TextField()
    booksandmovies_link = models.TextField()
    booksandmovies_remark = models.TextField()
