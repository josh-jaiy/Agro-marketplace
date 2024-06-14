from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Seller, Buyer
from crispy_bootstrap5.bootstrap5 import FloatingField



class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_seller', 'is_buyer']

class SellerProfileForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['company_name']

class BuyerProfileForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['contact_number']


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['company_name']