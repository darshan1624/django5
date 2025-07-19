from django import forms 
from account.models import User

class RegisterationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'confirm_password']
        
    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            self.add_error('confirm_password','Password didnt match')
        return cleaned_data
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email exists')
        return email