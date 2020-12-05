from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    phone = models.CharField(max_length=15)
    address = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_profiles'

    def __str__(self):
        return self.user.username


class District(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'districts'

    def __str__(self):
        return self.name


class DistrictData(models.Model):
    image = models.ImageField()
    day = models.CharField(max_length=100)
    period = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    avg_num_cars = models.TextField()
    avg_speed_cars = models.TextField()
    jam_time = models.TextField()

    class Meta:
        db_table = 'districts_data'

    def __str__(self):
        return f'{self.district.name} + {self.period}'
