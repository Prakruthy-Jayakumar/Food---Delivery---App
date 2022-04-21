from django.urls import path, include
from authentication_app import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('ordernow/', views.order, name='order'),
    path('logout/', views.logout, name='logout'),
    path('ordersucess/', views.successOrder, name='success'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities')

]
