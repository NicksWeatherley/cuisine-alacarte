from django.db import models
from app_user.models import User

class Customer(models.Model):
    '''
    Customer model is used for all customers in the cuisine alcarte project.
    Default behavior is to add a visitor upon checkout with and order that was
    completed.
    '''
    # Options for the customer type
    CUSTOMER_TYPES = [
        ('VISITOR', 'Visitor'),
        ('REGISTERED', 'Registered'),
        ('VIP', 'VIP'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    customer_type = models.CharField(max_length = 11, choices = CUSTOMER_TYPES, default = 'VISITOR')
    first_name = models.CharField(max_length=20, blank = True, default = '')
    last_name = models.CharField(max_length=20, blank = True, default = '')
    customer_email = models.CharField(max_length=100, blank = True, default = '')

    # Each customer has multiple ratings to multiple restaurants.
    restaurant_ratings = models.ManyToManyField('ratings.Rating', blank = True)
    restaurant = models.ForeignKey('restaurant.Restaurant', on_delete = models.SET_NULL, null = True)


    #TODO: Create many to many relation to ratings through delivery person

    #TODO: Create many to many relation to menu item through restaurant
    
    def __str__(self):
        if(self.customer_type == 'VISITOR'):
            return str(self.customer_type)

        return self.first_name + ' ' + self.last_name


