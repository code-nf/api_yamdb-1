from django.db import models


class Categories(models.Model):
    name = models.TextField(max_length=256)
    slug = models.SlugField(max_length=50,unique=True)

    def __str__(self):
        return self.name
