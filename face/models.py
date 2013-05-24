from django.db import models

# Create your models here.

class Tile(models.Model):
    z = models.IntegerField(db_index=True)
    x = models.IntegerField(db_index=True)
    y = models.IntegerField(db_index=True)

    # explored = models.BooleanField()

    # image = models.ImageField('photos/%Y/%m/%d')