from rest_framework import serializers
from .models import Theater, Screen, Movie, WeeklySchedule, WeeklyUnavailability, CustomUnavailability


class TheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theater
        fields = ["id", "name", "location"]


class ScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screen
        fields = ["id", "name", "theater"]
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "duration"]

class WeeklyScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklySchedule
        fields = ["day_of_week", "open_time", "close_time"]


class WeeklyUnavailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyUnavailability
        fields = ["day_of_week", "start_time", "end_time"]


class CustomUnavailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUnavailability
        fields = ["screen", "date", "start_time", "end_time", "full_day"]
