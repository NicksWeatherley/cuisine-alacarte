"""cuisine_alacarte URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('register.urls')),
    path('', include('pages.urls')),

    # Using re_path due to reverse lookup error
    re_path('', include(('customer.urls', 'customer'),
                        namespace='customer')),
    re_path('', include(('delivery_person.urls', 'delivery_person'),
                        namespace='delivery_person')),
    re_path('', include(('manager.urls', 'manager'),
                        namespace='manager')),
    re_path('', include(('ratings.urls', 'ratings'),
                        namespace='ratings')),
    re_path('', include(('salesperson.urls', 'salesperson'),
                        namespace='salesperson')),
    re_path('', include(('cook.urls', 'cook'),
                        namespace='cook')),

    # gives access to django log-in/out pages
    path('', include("django.contrib.auth.urls")),

]