from django.db import models

# Create your models here.
class Reviews(models.Model):
    name = models.CharField(max_length=300)
    content = models.CharField(max_length=300)