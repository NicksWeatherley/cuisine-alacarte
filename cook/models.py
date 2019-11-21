from django.db import models

# Create your models here.

class Cook(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    ssn = models.CharField(max_length=9)
#   where they work, will reference restaurants table
    restaurant = models.ForeignKey('restaurant.Restaurant')
#   rating (0 - 5) will reference Rating table/app
    rating = models.ForeignKey('ratings.Rating') # referencing model defined in different app
#   if cook gets warned more than 3 times they get a warning
    warnings = models.IntegerField()
    salary = models.FloatField()


# we should keep records of salaries, ratings, warnigns

