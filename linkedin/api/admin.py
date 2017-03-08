from django.contrib import admin
from api.models import data , Saved , Users , login

# Register your models here.

admin.site.register(data)
admin.site.register(Saved)
admin.site.register(Users)
admin.site.register(login)