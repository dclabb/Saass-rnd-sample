from django.db import models

#PageVisits is being called evertime beeing saved or create in the views.py.
class PageVisit(models.Model): #this will gonna be a table
    #this will be mapped into database table, path and tamestamp is a column so when you add data in the both it will be Rows
    #there will be ID foreign key automatically, is a primary key
    path = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True) #when it happens
    