from . import views
from django.urls import path

app_name = 'lodapp'


urlpatterns = [

    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('registration_form/',views.registration_form,name='registration_form'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('success/', views.success, name='success'),

]