from django.db import models


class Rating(models.Model):
    score = models.FloatField()
    note = models.CharField(
        max_length=120,
        blank=True,
        default="",
        )

    # Keeping this here as not to force clear migrations or DB, but not needed
    resturant = models.ForeignKey(
        "restaurant.Restaurant",
        on_delete=models.SET_NULL,
        null=True, blank=True,
    )
