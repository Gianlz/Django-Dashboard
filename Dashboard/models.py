from django.db import models
from django.utils import timezone

class RiverHeight(models.Model):
    height = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Height: {self.height} on {self.date}"