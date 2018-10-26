from django import forms 
from .models import TodoList, Category

from django.db import OperationalError

try:
    CHAT_BOT_USER, created = User.objects.get_or_create(username='rosty', email=settings.EMAIL_HOST_USER)

except OperationalError:
    CHAT_BOT_USER = None

if created:
    CHAT_BOT_USER.set_password(settings.EMAIL_HOST_PASSWORD)
    CHAT_BOT_USER.save()

class TodoForm(forms.Form):
    text = forms.CharField(max_length=40, 
        widget=forms.TextInput(
attrs={'class' : 'form-control', 'placeholder' : 'Enter todo e.g. Delete junk files', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}))
