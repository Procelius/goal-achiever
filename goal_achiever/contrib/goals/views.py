from django.shortcuts import (render, HttpResponseRedirect, get_object_or_404,
                              redirect, )
from django.contrib.auth.decorators import login_required

from .models import Goal, Task, Restriction
from .forms import GoalForm, TaskForm, RestrictionForm


@login_required
def goal_list(request):
    user = request.user
    if request.POST:
        form_type = request.POST["form_type"]
        form = _get_form(form_type)(data=request.POST, user=user)
        if form.is_valid():
            item = form.save()
            item.user = user
            item.save()
        return HttpResponseRedirect("/goal_achiever/")
    else:
        # Forms
        goal_form = GoalForm(user=user)
        task_form = TaskForm(user=user)
        restriction_form = RestrictionForm(user=user)
        # Items
        goals = Goal.objects.filter(user=user)
        tasks = Task.objects.filter(user=user)
        restrictions = Restriction.objects.filter(user=user)

    context = {
        "goals": goals,
        "tasks": tasks,
        "restrictions": restrictions,
        "goal_form": goal_form,
        "task_form": task_form,
        "restriction_form": restriction_form,
    }
    return render(request, "goals/goal_list.html", context)


@login_required
def edit_item(request, item_type, pk):
    user = request.user
    item_class = _get_class(item_type)
    item_form = _get_form(item_type)
    item = get_object_or_404(item_class, pk=pk)
    if request.method == "POST":
        if request.POST.get('edit'):
            form = item_form(data=request.POST, user=user, instance=item)
            if form.is_valid():
                form.save()
        elif request.POST.get('delete'):
            item.delete()
        else:
            raise Exception('Wrong request!', request.POST.values)
        return redirect('goal_list')
    else:
        form = item_form(user=user, instance=item)
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
