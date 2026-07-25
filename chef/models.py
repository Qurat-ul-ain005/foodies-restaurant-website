from django.db import models

class Chef(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.name