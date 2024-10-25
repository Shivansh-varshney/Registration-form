from django import forms
from django.contrib.auth.models import User
from .models import *

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-input'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-input'}))
    class Meta:
        model = User
        fields = ['username','email']

class FamilyDetailsForm(forms.ModelForm):
    class Meta:
        model = Family_detail
        exclude = ['username']

class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = Personal_detail
        exclude = ['username']

class SchoolDetailsForm(forms.ModelForm):
    class Meta:
        model = school_detail
        exclude = ['username']

class SubjectMarksForm(forms.ModelForm):
    class Meta:
        model = subject_mark
        exclude = ['username']

class BankDetailsForm(forms.ModelForm):
    class Meta:
        model = bank_detail
        exclude = ['username']