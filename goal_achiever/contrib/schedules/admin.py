from django.contrib import admin

from . import models

admin.site.register(models.TimePeriod)
admin.site.register(models.DaySchedule)
