#The purpose of this class is to give access to the models to admins on the admin page.
#This allows the admin to edit, delete and add data to the model saved in the database.

from django.contrib import admin
from .models import Incident

admin.site.register(Incident)
