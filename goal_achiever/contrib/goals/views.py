from django.shortcuts import (render, HttpResponseRedirect, get_object_or_404,
                              redirect, )

from .models import Goal, Task, Restriction
from .forms import GoalForm, TaskForm, RestrictionForm


def goal_list(request):
    if request.POST:
        form_type = request.POST["form_type"]
        form = _get_form(form_type)(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/goal_achiever/")
    else:
        goal_form = GoalForm()
        task_form = TaskForm()
        restriction_form = RestrictionForm()
        goals = Goal.objects.all()
        tasks = Task.objects.all()
        restrictions = Restriction.objects.all()

    context = {
        "goals": goals,
        "tasks": tasks,
        "restrictions": restrictions,
        "goal_form": goal_form,
        "task_form": task_form,
        "restriction_form": restriction_form,
    }
    return render(request, "goals/goal_list.html", context)


def edit_item(request, item_type, pk):
    item_class = _get_class(item_type)
    item_form = _get_form(item_type)
    item = get_object_or_404(item_class, pk=pk)
    if request.method == "POST":
        if request.POST.get('edit'):
            form = item_form(request.POST, instance=item)
            if form.is_valid():
                form.save()
        elif request.POST.get('delete'):
            item.delete()
        else:
            raise Exception('Wrong request!', request.POST.values)
        return redirect('goal_list')
    else:
        form = item_form(instance=item)
    context = {
        "form": form,
        "item": item,
    }
    return render(request, "goals/edit_item.html", context)


def _get_class(class_name):
    classes_dict = {
        "goal": Goal,
        "task": Task,
        "restriction": Restriction,
    }
    return classes_dict[class_name]


def _get_form(class_name):
    forms_dict = {
        "goal": GoalForm,
        "task": TaskForm,
        "restriction": RestrictionForm,
    }
    return forms_dict[class_name]
