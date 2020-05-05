from django.db import models
from django.contrib.auth.models import User

from goal_achiever.contrib.goals.models import Task


class ScheduleBase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    schedule_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class DaySchedule(ScheduleBase):
    pass


class TimePeriod(models.Model):
    day_schedule = models.ForeignKey(DaySchedule, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    start = models.TimeField(verbose_name="Start time")
    end = models.TimeField(verbose_name="End time")
    duration = models.TimeField(verbose_name="Duration")

    def __str__(self):
        return self.task.name if self.task else "Empty"
