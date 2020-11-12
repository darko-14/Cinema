from django.urls import path
from . import views
from .views import BookingView, BuyView, ConfirmView

urlpatterns = [
    path('movies/post/<int:pk>/booking/', BookingView.as_view(), name='booking-site'),
    path('movies/post/<int:pk>/booking/buy/', BuyView.as_view(), name='buy-site'),
    path('movies/post/<int:pk>/booking/buy/confirm/', ConfirmView.as_view(), name='confirm-site'),
]