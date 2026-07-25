from django.db import models

class Reservation(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    guests = models.IntegerField()

    date = models.DateField()

    time = models.TimeField()

    message = models.TextField(blank=True)

    def __str__(self):
        return self.name