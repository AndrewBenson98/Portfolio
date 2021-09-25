from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Name",max_length=50)
    email = forms.EmailField(label='E-mail Address',max_length=254)
    subject = forms.CharField(label='Subject',max_length=254)
    text = forms.CharField(label='Message',widget=forms.Textarea)
