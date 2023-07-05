from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, viewsets, permissions

from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking 


# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {})

class bookingview(APIView):
    def get(self, request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many = True)
        return Response(serializer.data)

class menuview(APIView):
    def post(self, request):
        serializer = MenuSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data":serializer.data})

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated] 