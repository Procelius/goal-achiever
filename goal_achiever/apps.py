from django.apps import AppConfig

path = "goal_achiever.contrib."


class Goals(AppConfig):
    name = path + "goals"
    verbose_name = "Goals"


class Schedules(AppConfig):
    name = path + "schedules"
    verbose_name = "Schedules"
