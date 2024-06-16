from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('news_updates/', views.newsandupdates, name='newsandupdates'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('help/', views.help, name='help'),
    path('add_match', views.add_match, name='add_match'),
    path('scoreboard/toss/matchnumber<int:match_number>/', views.toss, name='toss'),
    path('scoreboard/matchnumber<int:match_number>/<str:team_name>', views.scoreboard, name='scoreboard'),
]
