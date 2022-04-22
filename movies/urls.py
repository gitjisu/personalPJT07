from .import views
from django.urls import path


urlpatterns = [
    path('actors/', views.actor_list),
    path('actors/<int:actors_pk>/', views.actor_detail),
]
