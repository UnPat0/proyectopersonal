
from django.urls import path, include

from user.views import user_login, user_profile, user_register, user_logout

urlpatterns = [
    path('login/', user_login),
    path('register/', user_register),
    path('profile/', user_profile),
    path('logout/', user_logout),
    
]