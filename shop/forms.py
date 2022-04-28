from django import forms
from django.forms import ModelForm
from .models import Contact, Product





class Add_product_form(ModelForm):
    class Meta:
        model = Product
        fields='__all__'
        widgets = {
        }
       
        

       
        


        

        
