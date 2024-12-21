from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Imagen(models.Model):
    
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    
    imagen = models.ImageField(update_to = "imagenes", blank=True, null = True)
    
    def __str__(self):
        
        return f'Imagen de {self.user} - {self.imagen}'