from django.contrib import admin
from django.urls import path
from travel import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('', views.travel_list, name='travel_list'),
    path('book/<int:pk>/', views.book_travel, name='book_travel'),
    path('bookings/', views.my_bookings, name='my_bookings'),
    path('cancel/<int:pk>/', views.cancel_booking, name='cancel_booking'),
]
