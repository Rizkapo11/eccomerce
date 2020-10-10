from django.urls import path
from . import views
app_name = "store"
urlpatterns = [
        path ('', views.store, name= 'store'),
        path ('<Cart>/', views.Cart, name= 'Cart'),
        path ('<checkout>/', views.checkout, name= 'checkout'),
    ]