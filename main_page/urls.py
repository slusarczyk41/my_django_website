import sys

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
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote')
]