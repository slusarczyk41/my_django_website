from django.urls import path

from . import views

app_name = 'main_page'
urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('valuation/', views.valuation, name='valuation'),
    path('contact_endpoint/', views.contact_endpoint, name='contact_endpoint'),
    path('download_cv_endpoint/', views.download_cv_endpoint, name='download_cv_endpoint'),
]