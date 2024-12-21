from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from user.forms import UserRegisterForm, UserUpdateForm

from user.models import Imagen

from django.contrib.auth.decorators import login_required

# Create your views here.

def user_login(request):
    
    msg_login = "" 
    
    if request.method == 'POST':
        
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contrasenia)
            
            if user is not None:
                
                login(request, user)
                return render(request, "user/index.html" ) 
            
            msg_login = "usuario o contraseña incorrectos"
            
    form = AuthenticationForm()
            
    return render(request, 'users/login.html', {'form': form,'msg_login': msg_login})


def user_register(request):
    mesg_register = ""
    
    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            return render(request, 'users/index.html')
        
        mesg_register = "Error al registrar al usuario"
        
    form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form': form,'mesg_register': mesg_register})


@login_required 
def user_profile(request):
    
    usuario = request.user
    
    if request.method == 'POST':
        
        form = UserUpdateForm(request.POST, request.FILES , instance=usuario)
        
        if form.is_valid():
            
            if form.cleaned_data.get('image'):
                
                if Imagen.objects.filter(user=usuario).exists():
                    
                    usuario.imagen.imagen = form.cleaned_data('imagen')
                    
                    usuario.imagen.save()
                
                else: 
                    avatar = Imagen(user=usuario, imagen=form.changed_data.get('imagen'))
                    
                    avatar.save()
            
            form.save()
            
            return render(request, 'blog/index.html')
        
    
    else: 

        form = UserUpdateForm(instance = usuario)
        
        
@login_required       
def user_logout(request):
    
    logout(request)
    return redirect('login')



    
    
            