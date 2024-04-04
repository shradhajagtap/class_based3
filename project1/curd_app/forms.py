from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

        widgets = {
            "student_first_name": forms.TextInput(attrs={"class": "form-control"}),
            "student_last_name": forms.TextInput(attrs={"class": "form-control"}),
            "student_age": forms.NumberInput(),
            "student_address": forms.Textarea(attrs={"class": "form-control", 'rows': 4, 'cols': 15}),
            "student_div": forms.TextInput(attrs={"class": "form-control"})
        }
