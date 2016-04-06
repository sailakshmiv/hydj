from django.db import models

class Contents(models.Model):
    ids = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()