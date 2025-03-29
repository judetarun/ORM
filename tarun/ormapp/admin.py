from django.contrib import admin
from .models import book,BookAdmin
admin.site.register(book,BookAdmin)