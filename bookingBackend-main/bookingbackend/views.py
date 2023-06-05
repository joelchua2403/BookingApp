from django.shortcuts import render
from rest_framework import generics, status
from .models import Booking, Date
from .serializers import BookingSerializer, CreateBookingSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view




# Create your views here.
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingListView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

@api_view(['GET'])
def getAllBookings(request):
    bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBooking(request, pk):
    booking = Booking.objects.filter(vesselName=pk)
    serializer = BookingSerializer(booking, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBookingById(request, pk):
    booking = Booking.objects.get(id=pk)
    serializer = BookingSerializer(booking, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getBookingByBerth(request, pk):
    booking = Booking.objects.filter(berth=pk)
    serializer = BookingSerializer(booking, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBookingByDate(request, date):
    booking = Booking.objects.filter(date_time=date)
    serializer = BookingSerializer(booking, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createBooking(request):
    data = request.data

    date_data = data['date_time']

    date = Date.objects.create(
        date=date_data['date'],
        time=date_data['time'],
    )

    booking = Booking.objects.create(
        vesselName=data['vesselName'],
        berth=data['berth'],
        date_time=date,
        message=data['message'],
        activity=data['activity'],
        pilot=data['pilot'],
        tug=data['tug']
    )

    serializer = CreateBookingSerializer(booking, many=False)
    return Response(serializer.data)



@api_view(['PUT'])
def updateBooking(request, pk):
    booking = Booking.objects.get(id=pk)
    serializer = BookingSerializer(instance=booking, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteBooking(request, pk):
    booking = Booking.objects.get(id=pk)
    booking.delete()
    return Response('Booking deleted successfully!')