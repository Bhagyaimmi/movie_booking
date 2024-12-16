from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import (
    Theater, Screen, WeeklySchedule, WeeklyUnavailability, CustomUnavailability
)
from .serializers import (
    WeeklyScheduleSerializer, WeeklyUnavailabilitySerializer, CustomUnavailabilitySerializer
    
)
from .models import Theater, Screen, Movie
from .serializers import TheaterSerializer, ScreenSerializer, MovieSerializer

class TheaterCreateView(APIView):
    def post(self, request):
        serializer = TheaterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class MovieCreateView(APIView):
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ScreenCreateView(APIView):
    def post(self, request):
        serializer = ScreenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TheaterAvailabilityView(APIView):
    def post(self, request, id):
        theater = Theater.objects.get(id=id)
        data = request.data

        # Weekly schedule
        weekly_schedule = data.get("weekly_schedule", {})
        for day, schedule in weekly_schedule.items():
            WeeklySchedule.objects.update_or_create(
                theater=theater, day_of_week=day,
                defaults={
                    "open_time": schedule["open"],
                    "close_time": schedule["close"],
                }
            )

        # Weekly unavailability
        weekly_unavailability = data.get("weekly_unavailability", {})
        for day, unavailabilities in weekly_unavailability.items():
            for period in unavailabilities:
                WeeklyUnavailability.objects.update_or_create(
                    theater=theater, day_of_week=day,
                    start_time=period["start"],
                    end_time=period["end"],
                )

        return Response({"message": "Weekly schedule and unavailability configured successfully."})


class CustomUnavailabilityView(APIView):
    def post(self, request, id):
        theater = Theater.objects.get(id=id)
        data = request.data

        for slot in data.get("unavailable_slots", []):
            screen_id = data.get("screen_id")
            screen = Screen.objects.get(id=screen_id)
            CustomUnavailability.objects.create(
                theater=theater,
                screen=screen,
                date=slot["date"],
                start_time=slot["start"],
                end_time=slot["end"],
            )

        for date in data.get("unavailable_dates", []):
            screen_id = data.get("screen_id")
            screen = Screen.objects.get(id=screen_id)
            CustomUnavailability.objects.create(
                theater=theater,
                screen=screen,
                date=date,
                full_day=True,
            )

        return Response({"message": "Custom unavailability added successfully."})



class SlotView(APIView):
    def get(self, request, id):
        theater = Theater.objects.get(id=id)
        screen_id = request.query_params.get("screen_id")
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")

        # Validate input
        if not screen_id or not start_date or not end_date:
            return Response({"error": "screen_id, start_date, and end_date are required."}, status=400)

        screen = Screen.objects.get(id=screen_id)
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

        # Fetch schedules and unavailability
        weekly_schedules = WeeklySchedule.objects.filter(theater=theater)
        weekly_unavailability = WeeklyUnavailability.objects.filter(theater=theater)
        custom_unavailability = CustomUnavailability.objects.filter(
            theater=theater,
            screen=screen,
            date__range=[start_date, end_date],
        )

        # Slot generation logic
        slots = []
        current_date = start_date
        while current_date <= end_date:
            # Fetch weekly schedule for the day
            day_name = current_date.strftime("%A")
            schedule = weekly_schedules.filter(day_of_week=day_name).first()
            if schedule:
                open_time = datetime.combine(current_date, schedule.open_time)
                close_time = datetime.combine(current_date, schedule.close_time)
                slot_duration = timedelta(minutes=120)  # Example: 2-hour slots

                # Generate slots
                current_time = open_time
                while current_time + slot_duration <= close_time:
                    end_time = current_time + slot_duration

                    # Check unavailability
                    unavailable = weekly_unavailability.filter(
                        day_of_week=day_name,
                        start_time__lte=current_time.time(),
                        end_time__gte=current_time.time()
                    ).exists() or custom_unavailability.filter(
                        date=current_date,
                        start_time__lte=current_time.time(),
                        end_time__gte=current_time.time()
                    ).exists()

                    slots.append({
                        "start_time": current_time.time(),
                        "end_time": end_time.time(),
                        "is_available": not unavailable
                    })
                    current_time = end_time

            current_date += timedelta(days=1)

        return Response({"slots": slots}, status=200)
