from django.shortcuts import render

from .models import Goal
from .forms import GoalForm


def goal_list(request):
    goals = Goal.objects.all()
    if request.POST:
        goal_form = GoalForm(request.POST)
        if goal_form.is_valid():
            goal_form.save()
    else:
        goal_form = GoalForm()

    context = {
        "goals": goals,
        "form": goal_form,
    }
    return render(request, "goals/goal_list.html", context)
