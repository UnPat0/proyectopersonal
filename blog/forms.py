from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Título de la publicación'  
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 5, 
                'placeholder': 'Escribe aquí el contenido de tu publicación'  
            }),
            'is_published': forms.CheckboxInput(attrs={
                'class': 'form-check-input'  
            }),
        }
        labels = {
            'title': 'Título',  
            'content': 'Contenido',  
            'image': 'Imagen',  
            'is_published': '¿Publicar?'
        }





