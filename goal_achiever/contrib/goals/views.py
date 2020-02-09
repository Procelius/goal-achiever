from django.shortcuts import render

from .models import Goal


def goal_list(request):
    goals = Goal.objects.all()
    context = {
        "goals": goals,
    }
    return render(request, "goals/goal_list.html", context)
