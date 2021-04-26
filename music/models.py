from django.db import models


class Band(models.Model):
    origin = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=200)
    genre = models.ForeignKey("Genre", on_delete=models.SET_NULL, null=True)
    start_year = models.DateField(null=True)
    label = models.CharField(max_length=100)
    members = models.CharField(max_length=500, null=True)


class Album(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=500)
    slug = models.SlugField(max_length=100, null=True)
    asin = models.CharField(max_length=100, unique=True)
    release_date = models.DateField()
    band = models.ForeignKey("Band", on_delete=models.SET_NULL, null=True)
    cover = models.CharField(max_length=200)
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True)


class Music(models.Model):
    band = models.ForeignKey("Band", on_delete=models.SET_NULL, null=True)
    album = models.ForeignKey("Album", on_delete=models.SET_NULL, null=True)


class Genre(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.title
