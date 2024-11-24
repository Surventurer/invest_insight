from django.urls import path
from . import views
from .views import calculate_rd, calculate_fd

urlpatterns = [
    path('', views.home, name='home'),
    path('sip-calculator/', views.sip_calculator, name='sip_calculator'),
    path('fd_and_rd/', views.fd_and_rd, name='fd_and_rd'),
    path('real-estate/', views.real_estate, name='real_estate'),
    path('commodities/', views.commodities, name='commodities'),
    path('rd/', views.rd_page, name='rd_page'),
    path('fd/', views.fd_page, name='fd_page'),
    path('calculate_rd/', calculate_rd, name='calculate_rd'),
    path('calculate_fd/', calculate_fd, name='calculate_fd'),
]

