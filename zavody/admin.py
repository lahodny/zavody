from django.contrib import admin

# Import všech modelů, které obsahuje models.py

from .models import *

# Registrace modelů v administraci aplikace

admin.site.register(Zavod)
admin.site.register(Film)

