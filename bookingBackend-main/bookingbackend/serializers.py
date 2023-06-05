from rest_framework import serializers
from .models import Booking, Date


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = ('id', 'date', 'time')

class BookingSerializer(serializers.ModelSerializer):
    date_time = DateSerializer()
    class Meta:
        model = Booking
        fields = '__all__'

class CreateBookingSerializer(serializers.ModelSerializer):
    date_time = DateSerializer()
    class Meta:
        model = Booking
        fields = ('vesselName', 'berth', 'date_time', 'message', 'activity', 'pilot', 'tug')
    def create(self, validated_data):
        date_time_booking = validated_data.pop('date_time')
        booking = Booking.objects.create(**validated_data)
        for date_time in date_time_booking:
            Date.objects.create(booking=booking, **date_time)
       
        return booking