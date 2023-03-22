from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexview,name = 'index'),
    path('register_as_service_provider',views.register_as_service_provider,name = 'inderegister_as_service_provider'),
    path('signup',views.signup,name = 'signup'),
    path('login',views.login,name = 'login'),
    path('logout',views.handlelogout,name = 'logout'),
    path('book',views.book,name = 'book'),
]