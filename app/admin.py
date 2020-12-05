from django.contrib import admin

# Register your models here.
from app.models import UserProfile, District, DistrictData

admin.site.register(UserProfile)
admin.site.register(District)
admin.site.register(DistrictData)
