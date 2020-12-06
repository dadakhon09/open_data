from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from app.models import UserProfile, District, DistrictData
from app.serializers import UserProfileSerializer, DistrictSerializer, DistrictDataSerializer


class UserProfileListAPIView(ListAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.all()


class DistrictListAPIView(ListAPIView):
    serializer_class = DistrictSerializer

    def get_queryset(self):
        return District.objects.all()


class DistrictDataListAPIView(ListAPIView):
    serializer_class = DistrictDataSerializer

    def get_queryset(self):
        data = DistrictData.objects.all()
        if self.request.GET.get('day'):
            data = data.filter(day=self.request.GET.get('day'))
        if self.request.GET.get('period'):
            data = data.filter(period=self.request.GET.get('period'))
        return data


class SingleDistrictDataListAPIView(APIView):
    serializer_class = DistrictDataSerializer

    def get(self, district_id):
        dis = District.objects.get(id=district_id)
        return DistrictData.objects.filter(district=dis)
