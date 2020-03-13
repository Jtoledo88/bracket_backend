from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.ServiceList.as_view()),
    path('services/<int:pk>/edit', views.ServiceUpdate.as_view()),
    path('events/', views.EventList.as_view()),
    path('events/<int:pk>/edit', views.EventUpdate.as_view()),
]