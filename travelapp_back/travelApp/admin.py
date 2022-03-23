from django.contrib import admin
from .models.account import Account
from .models.user import User
from .models.bookings import Bookings
from .models.flights import Flights


# Register your models here.
admin.site.register(User)
admin.site.register(Account)
admin.site.register(Bookings)
admin.site.register(Flights)
