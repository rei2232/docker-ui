from django.db import models
import os


class Registry(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    instance_url = models.CharField(max_length=200)
    project_path = models.CharField(max_length=200)
    authentication = models.BooleanField(default=False)

    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return os.path.join(self.instance_url, self.project_path)
