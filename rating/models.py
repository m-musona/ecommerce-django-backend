from django.db import models

# Create your models here.

class Rating(models.Model):
    id = models.CharField(max_length=50, blank=False, primary_key=True)

    def __str__(self):
        return self.id
