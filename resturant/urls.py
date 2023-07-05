from django.urls import path
from .views import index, menuview,bookingview, SingleMenuItemView, MenuItemsView, BookingViewSet
urlpatterns = [
    path('', index, name='index'),
    path('menue/', menuview.as_view()),
    path('booking/', bookingview.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('menu/items', MenuItemsView.as_view()),



]
