from django.contrib import admin 
from django.urls import path 
from . import views 
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [ 
    path('', views.index, name='index'), 
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('bookings/', views.BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='booking-list'),
    path('bookings/<int:pk>', views.BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='booking-detail'),
    path('api-token-auth/', obtain_auth_token),
]