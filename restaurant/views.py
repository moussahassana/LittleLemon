from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView,DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import MenuItem,Booking
from .serializers import MenuItemSerializer,BookingSerializer

class MenuItemView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateAPIView,DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
# View for rendering the index page
def index(request):
    return render(request, 'index.html', {})
