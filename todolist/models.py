from django.db import models
from django.utils import timezone
import os

class Category(models.Model): 
    name = models.CharField(max_length=100) 

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name


class TodoList(models.Model): 
  
     
    

    title = models.CharField(max_length=250)
    content = models.TextField(blank=True) 
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) 
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) 
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default="general")
    #image= models.ForeignKey(Image,on_delete=models.CASCADE)  
    image= models.FileField(upload_to='images/', null=True)
   

    class Meta:
        ordering = ["-created"] 

    def __str__(self):
        return self.title 


     



   
