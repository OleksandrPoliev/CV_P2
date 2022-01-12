from django import forms
from .models import Contact
from django.forms import ModelForm
class ContactForm(ModelForm):
    Company = forms.CharField(max_length=50)
    Email = forms.EmailField(required=True)
    Title=forms.CharField(max_length=100)
    Message=forms.CharField(widget=forms.Textarea,max_length=2000)

    class Meta:
        model = Contact
        fields = '__all__'


