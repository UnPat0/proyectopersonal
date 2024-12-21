from django.urls import path

from blog.views import agregar_post, edit_post, delete_post, blog_list

urlpatterns = [
    path('', blog_list ),
    path('agregar/', agregar_post),
    path('editar/<int:post_id>/', edit_post),
    path('eliminar/<int:post_id>/', delete_post),

    
]