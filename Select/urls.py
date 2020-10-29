from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.login,name='login'),
    path('home', views.index,name='home'),
    path('default',views.default,name='default'),
	path('validate',views.validate,name='validate'),
	path('save/<int:pid>',views.save,name='save'),
]
