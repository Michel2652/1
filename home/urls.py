from django.urls import path
from . import views


urlpatterns = [
    path('hello/', views.h,name='hello') ,
    path('bye/', views.g) ,
    path('profile/<x>/',views.x,name='profile'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('create/' , views.create,name='create'),
    path('update/<p_id>/',views.update,name='update'),
    path('',views.welcom)
]