from django.forms import ModelForm
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description','duedate', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class':      'form-control', 'placeholder': 'write a title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'write a description'}),
            'duedate': forms.DateInput (attrs={'class':      'form-control', 'placeholder': 'yyyy-mm-dd'}),

            'important': forms.CheckboxInput(attrs={'class': 'form-check-input m-bottom'}),
        }
