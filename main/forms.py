from django import forms

class FormBid(forms.Form):

    name = forms.CharField(max_length=100, required=True, label='ФИО')
    email = forms.EmailField(required=True, label='Email')
    phone = forms.CharField(empty_value='+7', max_length=15, required=True)