from django import forms
from .models import Customer, Car

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('name', 'email', 'birth_date',)

class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ('color', 'brand', 'purchase_date', 'customer',)
