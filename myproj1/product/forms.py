from django import forms
from product.models import Product

class Addproduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','description']