from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Vice_Captain(models.Model):
    name = models.CharField(max_length = 50)
    image = models.ImageField()
    votes = models.IntegerField()
    vice_captain_slug = AutoSlugField(populate_from = 'name')

    def __str__(self):
        return self.name
