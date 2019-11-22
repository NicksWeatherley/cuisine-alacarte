from django.db import models

# Create your models here.

#Registered_Customers inherit from Visitor and VIP_Customer inherit from Registerd_Customer
class Visitor(models.Model):
    customer_id = models.CharField(max_length=10)

class Registered_Customer(Visitor):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    customer_email = models.CharField(max_length=100)
#   rating (0-5) will reference Rating table/app
    rating = models.ForeignKey('ratings.Rating', on_delete = models.CASCADE)
#   if customer gives an average rating >4 for more than 3 orders they're promoted to VIP_Customer
#   if customer gives an average rating <2 but >1 for more than 3 orders they're demoted to Visitor
#   if customer gives an average rating 1 then they are blacklisted

class VIP_Customer(Registered_Customer):
    customer_status = models.CharField(max_length=10)

