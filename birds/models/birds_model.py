from django.db import models
from users.services.upload_files import upload_name


class Birds(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_name, null=True, blank=True)

    def __str__(self):
        return self.name

