from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_short_url, name='create_short_url'),
    path('<str:short_url>/', views.redirect_to_original_url, name='redirect_to_original_url'),
    path('get_list', views.get_shortened_urls_list, name='get_url_list')
]
