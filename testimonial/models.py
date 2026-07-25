from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.name