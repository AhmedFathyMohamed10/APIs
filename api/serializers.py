from rest_framework.serializers import ModelSerializer
from .models import *

class GuestSerializer(ModelSerializer):
    class Meta:
        model = Guest
        fields = ['user_id', 'name', 'mobile', 'reservation']


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'