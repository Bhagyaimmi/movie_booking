from django.db import models
class Theater(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Screen(models.Model):
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, related_name="screens", default=1)  # Example default
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.theater.name} - {self.name}"
class Movie(models.Model):
    title = models.CharField(max_length=255)
    duration = models.IntegerField()  # in minutes

    def __str__(self):
        return self.title
class WeeklySchedule(models.Model):
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, related_name="weekly_schedules", default=1)
    day_of_week = models.CharField(max_length=10)  # e.g., Monday
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return f"{self.theater.name} - {self.day_of_week}"


class WeeklyUnavailability(models.Model):
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, related_name="weekly_unavailability", default=1)
    day_of_week = models.CharField(max_length=10)  # e.g., Monday
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.theater.name} - {self.day_of_week} Unavailable"


class CustomUnavailability(models.Model):
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, related_name="custom_unavailability",null=True, 
    blank=True) 
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, related_name="custom_unavailability")
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    full_day = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.theater.name} - {self.date} {self.start_time} to {self.end_time}"
    