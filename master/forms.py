# myapp/forms.py
from django import forms
from .models import Enquiry
from phonenumber_field.formfields import PhoneNumberField

class EnquiryForm(forms.ModelForm):

    class Meta:
        model = Enquiry
        fields = ['name', 'mobile_number', 'email', 'message']

    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input1', 'placeholder': 'Name'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input1', 'placeholder': 'Email'})
    )
    mobile_number = PhoneNumberField(
        required=True,
        error_messages={'required': 'Please enter your mobile number.'},
        widget=forms.TextInput(attrs={'class': 'input1', 'placeholder': 'Mobile Number'})
    )
    message = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input1', 'placeholder': 'Message'})
    )
