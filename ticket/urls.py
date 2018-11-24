"""ticket URL Configuration
"""
from django.conf.urls import url
from django.urls import path
from django.views.generic.base import TemplateView
from ticket import views

urlpatterns = [
    url(r'add/', views.ticket_add, name='ticket_add'),    
    # path(r'(?# ticket)/add/<int:ticket_id>/', views.ticket_vote, name='ticket_vote'),    
    path(r'view/<int:ticket_id>/', views.ticket_view, name='ticket_view'),    
    url(r'(?P<category>\w+)', views.index, name='index'),    
    url(r'', views.index, name='index'),    
]
