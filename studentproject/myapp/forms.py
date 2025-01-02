from django import forms
from .models import *
from django.core.exceptions import ValidationError


# used to get the data from the user and to store in our db:
class studentform(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'
    def clean_marks(self):
        mark=self.cleaned_data.get('marks')
        if mark>100:
            raise ValidationError('subject marks are out of 100 only')
        return mark


