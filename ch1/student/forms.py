from django import forms

class Registeration(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(initial='abcd@gmail.com')
    city = forms.CharField()
    key = forms.CharField(widget=forms.HiddenInput())


class LoginUser(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())



