from django.urls import path
from . import views

urlpatterns = [
    path('vista1/', views.vista1, name='vista1'),
    path('vista2/', views.vista2, name='vista2'),
    path('vista3/', views.vista3, name='vista3'),
    path('vista4/', views.vista4, name='vista4'),
    path('vista5/', views.vista5, name='vista5'),
    path('login/', views.login, name='login'),

]
