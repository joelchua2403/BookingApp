from django.urls import path
from . import views
from .views import BookingListView, BookingCreateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import MyTokenObtainPairView

urlpatterns = [
    path('view/all', views.getAllBookings, name='getAllBookings'),
    path('view/<str:pk>/', views.getBooking, name='getBooking'),
    path('view/id/<str:pk>/', views.getBookingById, name='getBookingById'),
    path('create/', views.createBooking, name='createBooking'),
     path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('update/<str:pk>/', views.updateBooking, name='updateBooking'),
    path('delete/<str:pk>/', views.deleteBooking, name='deleteBooking'),
    path('view/berth/<str:pk>/', views.getBookingByBerth, name='getBookingByBerth'),
    path('view/date/<str:pk>/', views.getBookingByDate, name='getBookingByDate'),
    
]
