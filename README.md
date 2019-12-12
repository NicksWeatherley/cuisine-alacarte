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
The current implementation of the code does not support maps, but can easily be implemented to handle new deliveries and the logic for it. The current purchase and delivery models are directly linked to a customer and delivery person. The logic is also present to change the delivery or purchase status to correctly match when a new delivery is added. The bidding system is in place for delivery people to bid. For the maps we were planning on using [mapbox](https://www.mapbox.com) for the maps and realtime routing. Implementation examples [here](https://www.fullstackpython.com/blog/maps-django-web-applications-projects-mapbox.html).

**2. Text-to-Speech Feature** -
The current implementation of the code does not support text-to-speech without breaking. Was unable to program text-to-speech efficiently in Django with dynamic html pages. The text-to-speech feature itself was handled with a python package [gTTs](https://pypi.org/project/gTTS/), and can be used to make audio files that will read static text, but not the data that depends on the user. The branch used to work on it is called tts. Solutions tried were requesting the page using bs4 requests (using both Beautiful Soup and html2text) to get the fully rendered page and convert it to text to be read. The function to read the text and play audio of that text is in the customer templatetags as customer_extra.py and the page that was being tested was customer/history_list.html . To fix it we just have to implement the third party package with our dynamic pages so that all the displayed text can be collected and read.

**3. Placing Orders** -
The current implementation for customers includes models for the Customer and the Order. Customers are able to see the page with all the restaurants and their menus and they can access the form of placing the orders. There are also pages for Shopping Cart and Order History. However, the current order form shows all the dishes (from all the restaurants, not from one restaurant that the customer wants to order from). Because we didn't bind the form to the specific restaurant, the Order object cannot be created and ordered cannot be added to shopping cart. To fix we would need to pass restaurant's id into the form through the view which is typically just two lines of code, but when doing so we're getting an ambiguous error. 
