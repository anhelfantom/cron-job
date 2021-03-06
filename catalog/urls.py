from django.urls import path, include
from . import views

app_name = 'cron'

urlpatterns = [
	path('accounts/', include('django.contrib.auth.urls')),
	path('<int:enabled>/',views.index, name='index'),
	path('',views.main, name='main'),
	path('submit',views.submit, name='submit'),
	path('login',views.login, name='login'),
	path('trylogin', views.tryLogin, name='tryLogin'),
    path('tryregister""', views.tryRegister, name='tryRegister'),
    path('register', views.register, name='register'),
	path('logout', views.logout, name='logout')
]
