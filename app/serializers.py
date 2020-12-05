from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from app.models import UserProfile, District, DistrictData


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserProfileSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'phone', 'address')


class DistrictSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class DistrictDataSerializer(ModelSerializer):
    district = DistrictSerializer()

    class Meta:
        model = DistrictData
        fields = ('id', 'district', 'image', 'day', 'period', 'avg_num_cars', 'avg_speed_cars', 'jam_time')
