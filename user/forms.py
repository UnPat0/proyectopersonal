from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="repetir contraseña", widget=forms.PasswordInput)
    
    class Meta:
        
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class UserUpdateForm(UserChangeForm):
    
    email = forms.EmailField(label="ingrese su correo electronico")
    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="repetir contraseña", widget=forms.PasswordInput)
    
    
    class Meta:
        
        model = User
        fields = ["email", "password1", "password2"]
        
        
        
