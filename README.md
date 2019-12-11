# cuisine-alacarte

Library/Language Requirements:
1. Python 3.x.x
2. Django
3. Crispy Forms

Steps to run locally:
1. Navigate to repo location in terminal
1. Call `python manage.py runserver`
2. Navigate to port provided in output
3. Enjoy!

***
# Missing Features

**1. Map Feature** - 
The current implementation of the code does not current support maps, but can easily be implemented to handle new deliveries and the logic for it. The current purchase and delivery models are directly linked to a customer and delivery person. The logic is also present to change the delvery or purchase status to correctly match when a new delivery is added and the bidding system in place for delivery people to bid. For the maps we were planning on using [mapbox](https://www.mapbox.com) for the maps and realtime routing. Implementation examples [here](https://www.fullstackpython.com/blog/maps-django-web-applications-projects-mapbox.html).
