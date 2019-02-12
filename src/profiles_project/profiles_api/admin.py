from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.UserProfile) #pass in created model, register with Django admin
