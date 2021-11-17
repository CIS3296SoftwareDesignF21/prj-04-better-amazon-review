from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('library/', views.library, name="library"),
]