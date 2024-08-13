from django import forms
from django.contrib.auth.models import User
from capp.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=["contact_name","contact_email","contact_phone"]
        widgets={
            "contact_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Name"}),
            "contact_email":forms.TextInput(attrs={"class":"form-control","placeholder":"Email"}),
            "contact_phone":forms.NumberInput(attrs={"class":"form-control","placeholder":"Phone"}),
            

        }
class UpdateContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=["contact_name","contact_email","contact_phone"]
        widgets={
            "contact_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Name"}),
            "contact_email":forms.TextInput(attrs={"class":"form-control","placeholder":"Email"}),
            "contact_phone":forms.NumberInput(attrs={"class":"form-control","placeholder":"Phone"}),
            

        }