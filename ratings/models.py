from django.db import models


class Rating(models.Model):
    score = models.FloatField()
    note = models.CharField(
        max_length=120,
        blank=True,
        default="",
        )
