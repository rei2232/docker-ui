from django.db import models
from images.models import Image


class Container(models.Model):
    container_id = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    image = models.ForeignKey(Image, on_delete=models.NOT_PROVIDED)
    envs = models.TextField(null=True)
    ports = models.TextField(null=True)
