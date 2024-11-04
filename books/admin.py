from django.contrib import admin

# Register your models here.

from .models import books  # Replace with your model name

admin.site.register(books)