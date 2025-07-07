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

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 4:
            raise forms.ValidationError('Enter more that 4 chars')
        return username

    def clean(self):
        # cleaned_data = super().clean()
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and len(email) < 20:
            self.add_error('email', 'Enter more than 5 chars.')
        
        if username and len(username) < 4:
            self.add_error('username', 'Enter more than 5 chars.')
        
        return self.cleaned_data

        



