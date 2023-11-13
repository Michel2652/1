from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.user_r,name='user_r'),
    path('login/',views.user_l,name='user_l'),
    path('logout/',views.user_out,name='user_out'),
]