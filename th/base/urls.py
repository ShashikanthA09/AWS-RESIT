from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('create-product/', views.create_product, name='create_product'),
    path('products/', views.product_list, name='product_list'),
    path('logout/', LogoutView.as_view(), name='logout'),


]

