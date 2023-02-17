from django import forms  
from .models import *
    
class Message_form(forms.ModelForm):
    class Meta:
        model=Message
        fields ='__all__'

 

class Registration_form(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        wedget={
            'phone':forms.NumberInput(),
        } 
        