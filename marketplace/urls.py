from django.urls import path, include
from . import views
from .views import get_started
#from django.contrib.auth import views as auth_views 
#from .forms import LoginForm
#app_name='marketplace'


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/buy/', views.buy_product, name='buy_product'),
    path('transaction/<int:pk>/', views.transaction_detail, name='transaction_detail'),
    path('register/', views.register, name='register'),
    path('seller/profile/', views.seller_profile, name='seller_profile'),
    path('seller/create/', views.create_seller_profile, name='create_seller_profile'),
    path('buyer/profile/', views.buyer_profile, name='buyer_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('get-started/', get_started, name='get_started'),
    path('seller/dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('buyer/dashboard/', views.buyer_dashboard, name='buyer_dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include auth URLs
    path('logout/', views.logged_out_view, name='logout'),
]

