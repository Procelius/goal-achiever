from django.shortcuts import render

from .models import Goal
from .forms import GoalForm, TaskForm, RestrictionForm


def goal_list(request):
    goals = Goal.objects.all()
    goal_form = GoalForm()
    task_form = TaskForm()
    restriction_form = RestrictionForm()
    if request.POST:
        action = request.POST["action"]
        if action == "new_goal":
            goal_form = GoalForm(request.POST)
            if goal_form.is_valid():
                goal_form.save()
        elif action == "new_task":
            task_form = TaskForm(request.POST)
            if task_form.is_valid():
                task_form.save()
        elif action == "new_restriction":
            restriction_form = RestrictionForm(request.POST)
            if restriction_form.is_valid():
                restriction_form.save()

    context = {
        "goals": goals,
        "goal_form": goal_form,
        "task_form": task_form,
        "restriction_form": restriction_form,
    }
    return render(request, "goals/goal_list.html", context)
