from django.db import models


class Categories(models.Model):
    name = models.TextField(max_length=256)
    slug = models.SlugField(max_length=50,unique=True)

    def __str__(self):
        return self.slug


class Genres(models.Model):
    name = models.TextField(max_length=256)
    slug = models.SlugField(max_length=50,unique=True)

    def __str__(self):
        return self.slug


class Titles(models.Model):
    name = models.TextField(max_length=256)
    year = models.IntegerField()
    description = models.TextField(blank=True)
    genre = models.ManyToManyField(Genres)
    category = models.ForeignKey(
        Categories, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name