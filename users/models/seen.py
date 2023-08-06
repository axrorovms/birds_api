from django.db import models
from users.models import User
from birds.models import Birds


class Seen(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bird = models.ForeignKey(Birds, on_delete=models.CASCADE)
