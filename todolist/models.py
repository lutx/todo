from django.db import models
from django.utils import timezone

class Category(models.Model): 
    name = models.CharField(max_length=100) 

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name 

class TodoList(models.Model): 
    def get_image_path(instance, filename):
        return os.path.join('photos', str(instance.id), filename)

    title = models.CharField(max_length=250)
    content = models.TextField(blank=True) 
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) 
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) 
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default="general") 
    task_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    class Meta:
        ordering = ["-created"] 

    def __str__(self):
        return self.title 

   
