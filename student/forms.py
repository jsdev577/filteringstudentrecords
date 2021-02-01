from django.forms import ModelForm,RadioSelect
from .models import Student



class StudentForm(ModelForm):
    class Meta:
        model=Student
        
        fields='__all__'
        widgets={'graduate':RadioSelect}