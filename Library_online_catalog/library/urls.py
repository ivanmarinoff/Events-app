from .import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile_create/', views.profile_create, name='profile_create'),
    path('profile_details/', views.profile_details, name='profile_details'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('profile_delete/', views.profile_delete, name='profile_delete'),
    path('event_create/', views.create_event, name='create_event'),
    path('event_details/<int:pk>/', views.details_event, name='details_event'),
    path('event_edit/<int:pk>/', views.edit_event, name='edit_event'),
    path('event_delete/<int:pk>/', views.delete_event, name='delete_event'),
]