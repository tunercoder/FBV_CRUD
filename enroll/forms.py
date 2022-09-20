from dataclasses import field
from tkinter import Widget
from django import forms
from .models import Student
from django.core import validators

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','roll','age','standard']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'roll':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'standard':forms.TextInput(attrs={'class':'form-control'})
        }