from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='astro-home'),
    path('about/', views.about, name='astro-about'),
    path('scorpio/', views.scorpio, name='scorpio'),
    path('aries/', views.aries, name='aries'),
    path('taurus/', views.taurus, name='taurus'),
    path('gemini/', views.gemini, name='gemini'),
    path('aquarius/', views.aquarius, name='aquarius'),
    path('cancer/', views.cancer, name='cancer'),
    path('capricorn/', views.capricorn, name='capricorn'),
    path('leo/', views.leo, name='leo'),
    path('libra/', views.libra, name='libra'),
    path('pisces/', views.pisces, name='pisces'),
    path('sagitarius/', views.sagitarius, name='sagitarius'),
    path('virgo/', views.virgo, name='virgo'),

]
