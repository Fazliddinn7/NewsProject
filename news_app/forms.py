from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'


class SubscriptionForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=250)
    message = forms.CharField()
        