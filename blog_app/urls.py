
from unicodedata import name
from django.urls import path
from blog_app import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.home),
    path('add-news/', views.add_news, name='add-news'),
    path('edit_news/<int:id>', views.edit_news, name='edit_news'),
    path('delete_news/<int:id>', views.delete_news, name='delete_news'),
    path('signin/',views.signin, name='signin'),
    path('register/', views.register, name='register'),
    path('signout/',views.signout,name='signout'),
    path('profile/',views.profile,name='profile'),
    path('password_reset/',views.password_reset,name='password_reset')
]