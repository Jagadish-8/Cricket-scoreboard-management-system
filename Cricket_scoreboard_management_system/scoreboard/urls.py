from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Pages().index, name = 'index'),
    path('news_updates/', views.Pages().newsandupdates, name='newsandupdates'),
    path('about/', views.Pages().about, name='about'),
    path('contact/', views.Pages().contact, name='contact'),
    path('help/', views.Pages().help, name='help'),
    path('add_match/', views.Pages().add_match, name='add_match')

]
