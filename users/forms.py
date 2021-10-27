from django import forms
from django.forms.widgets import EmailInput
from django.contrib.auth.models import User
from users.models import Profile

class ProfileForm(forms.Form):
    
    website = forms.URLField(max_length=100, required=False)
    bio = forms.CharField(max_length=500, required=True)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField(required=False)


class SignUpForm(forms.Form):
    
    username = forms.CharField(
        label=False, 
        min_length=4, 
        max_length=20, 
        widget = forms.TextInput(attrs={'placeholder':'username','class': 'form-control','required': True})
        )
    password = forms.CharField(
        label=False,
        min_length=6, 
        widget=forms.PasswordInput(attrs={'placeholder':'Password','class': 'form-control','required': True})
        )
    password_confirmation = forms.CharField(
        label=False,
        min_length=6, 
        widget=forms.PasswordInput(attrs={'placeholder':'Password Confirmation','class': 'form-control','required': True})
        )
    first_name = forms.CharField(
        label=False, 
        min_length=2, 
        max_length=50, 
        widget = forms.TextInput(attrs={'placeholder':'first_name','class': 'form-control','required': True})
        )
    last_name = forms.CharField(
        label=False, 
        min_length=2, 
        max_length=50,
        widget = forms.TextInput(attrs={'placeholder':'last_name','class': 'form-control','required': True})
        )
    email = forms.EmailField(
        label=False, 
        min_length=6, 
        max_length=100, 
        widget=EmailInput(attrs={'placeholder':'Email','class': 'form-control','required': True})
        )

    def clean_username(self):
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()

        if username_taken:
            raise forms.ValidationError('Username is already in use')

        return username

    def clean(self):
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords does not match')

        return data

    def save(self):
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()