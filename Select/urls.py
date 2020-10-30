from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.login,name='login'),
    path('home', views.index,name='home'),
	path('data', views.data,name='data'),
	path('validate',views.validate,name='validate'),
	path('save/<int:pid>',views.save,name='save'),
]
