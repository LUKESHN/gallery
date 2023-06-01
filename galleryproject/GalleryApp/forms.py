from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from.models import ImageModel


class RegisterForm(UserCreationForm):
    password1=forms.CharField(label='enter your password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}))

    password2=forms.CharField(label='confirmed Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirmed password'}))

    class Meta:
        model=User
        fields= ['first_name','last_name','username','email']
        labels={
            'first_name':'Enter your First name',
            'last_name':'Enter your Last name',
            'username':'Enter your username',
            'email':'Enter your Email-ID'
        }
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter first name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter last name'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'enter username'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'enter your email'}),
        }


class LoginForm(AuthenticationForm):
    username=forms.CharField(label='Enter Your Username',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter username','placeholder':'enter username'}))
    password=forms.CharField(label='Enter Your Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter password'}))

    class Meta:
        model=User
        fields={'username','password'}


class ImageForm(forms.ModelForm):
    class Meta:
        model=ImageModel
        fields=['title','cat','image','desc']
        labels={
            'title':'Enter image title',
            'cat':'enter image category',
            'image':'upload image',
            'desc':'enter image description'
        }
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'cat':forms.Select(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'})
        }