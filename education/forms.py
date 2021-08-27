from django import forms

from education.models import Student


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

