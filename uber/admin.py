from django.contrib import admin

# Register your models here.
from uber.models import Ride,User

# Register your models here.
admin.site.register(User)
admin.site.register(Ride)