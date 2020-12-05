from django.urls import path

from app.views import UserProfileListAPIView, SingleDistrictDataListAPIView, DistrictDataListAPIView, \
    DistrictListAPIView

urlpatterns = [
    path('user-profiles/', UserProfileListAPIView.as_view()),
    path('districts/', DistrictListAPIView.as_view()),
    path('districts-data/', DistrictDataListAPIView.as_view()),
    path('districts-data/<int:district_id>/', SingleDistrictDataListAPIView.as_view()),
]
