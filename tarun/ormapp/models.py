from django.db import models
from django.contrib import admin
class book(models.Model):
    name=models.CharField(max_length=30)
    author=models.CharField(max_length=50)
    pages=models.CharField(max_length=25)
    language=models.CharField(max_length=100)
    price=models.IntegerField()
    rating=models.FloatField()
class BookAdmin(admin.ModelAdmin):
    list_display=('name','author','pages','language','price','rating')