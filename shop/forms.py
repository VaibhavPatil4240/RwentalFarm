from django import forms
from django.forms import ModelForm
from .models import Product
from users.models import Account




class Add_product_form(ModelForm):
    class Meta:
        model = Product
        fields='__all__'
        widgets = {
        }
       
        

        

class Role_selection_form(ModelForm):
    class Meta:
        model = Account
        fields='__all__'
        widgets = {
        }
       
        

        
