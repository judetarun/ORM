# Ex02 Django ORM Web Application
# Date:29.03.2025
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# ENTITY RELATIONSHIP DIAGRAM
![alt text](<Screenshot 2025-03-28 001303[1].png>)
## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 books

# PROGRAM 
models.py
```
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
```
admin.py
```
from django.contrib import admin
from .models import book,BookAdmin
admin.site.register(book,BookAdmin)
```

# OUTPUT
![alt text](<Screenshot 2025-03-29 131133.png>)
![alt text](<Screenshot 2025-03-29 131159.png>)
![alt text](<Screenshot 2025-03-29 131237.png>)

# RESULT
Thus the program for creating a database using ORM hass been executed successfully
