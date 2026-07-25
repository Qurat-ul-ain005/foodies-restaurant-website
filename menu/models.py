from django.db import models

class Menu(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField()

    price = models.DecimalField(max_digits=8, decimal_places=2)

    category = models.CharField(max_length=50)

    image = models.CharField(max_length=255)

    def __str__(self):
        return self.name