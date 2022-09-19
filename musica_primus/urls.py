from django.urls import path
from musica_primus import views

urlpatterns = [
    path('', views.musica_primus, name='musica_primus'),
]