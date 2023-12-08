from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Profile,CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('name','email','address','phone_number',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo',)

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('name','email','address','phone_number','password1','password2')

        def clean_password2(self):
            cd=self.cleaned_data
            if cd['password1'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']
        
        def clean_email(self):
            email = self.cleaned_data.get('email')
            qs = CustomUser.objects.exclude(id=self.instance.id).filter(email=email)
            if qs.exists():
                raise forms.ValidationError("Email already exists")
            return email

class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter Email',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
    }))