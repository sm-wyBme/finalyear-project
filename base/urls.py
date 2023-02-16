from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name = 'home'),
	path('add/', views.addPointView, name = 'add-point'),
	path('subtract/', views.subtractPointView, name = 'subtract-point'),
	path('multiply/', views.multiplyPointView, name = 'multiply-point'),
	path('double/', views.doublePointView, name = 'double-point'),
]