from django.db import models


class Image(models.Model):
    repository = models.CharField(max_length=1000)
    image_id = models.CharField(max_length=100, null=True)
    image_short_id = models.CharField(max_length=100, null=True)
    tags = models.CharField(max_length=1000, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.repository
