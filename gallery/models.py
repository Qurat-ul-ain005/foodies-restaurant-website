from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.title