from django import forms
from django.forms import ModelForm

class DateInput(forms.DateInput):
      input_type = 'date'
      fields = 'date'