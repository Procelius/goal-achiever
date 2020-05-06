import datetime
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import TimePeriod, DaySchedule
from .forms import TimePeriodForm, DayScheduleForm


@login_required
def schedules(request):
    user = request.user
    if request.POST:
        form = DayScheduleForm(data=request.POST, user=user)
        if form.is_valid():
            day = form.save()
            day.user = user
            day.save()
        return HttpResponseRedirect("/goal_achiever/schedules/")
    form = DayScheduleForm(user=user)
    day_schedules = DaySchedule.objects.filter(user=user)
    context = {
        "form": form,
        "day_schedules": day_schedules,
    }
    return render(request, "schedules/schedules.html", context)


@login_required
def edit_day(request, pk):
    user = request.user
    instance = get_object_or_404(DaySchedule, pk=pk)
    if request.method == "POST":
        if request.POST.get('edit_day'):
            form = DayScheduleForm(data=request.POST, user=user, instance=instance)
            if form.is_valid():
                form.save()
        elif request.POST.get('delete_day'):
            instance.delete()
        elif request.POST.get('add_task'):
            form = TimePeriodForm(data=request.POST, user=user)
            if form.is_valid():
                data = form.data
                form.instance.duration = _calc_duration(data['start'], data['end'])
                form.instance.day_schedule = instance
                form.save()
                return redirect(request.path)
        else:
            raise Exception('Wrong request!', request.POST.values)
        return redirect('schedules')

    day_form = DayScheduleForm(user=user, instance=instance)
    day_task_form = TimePeriodForm(user=user)
    day_tasks = TimePeriod.objects.filter(day_schedule=instance)

    context = {
        "day_form": day_form,
        "day_task_form": day_task_form,
        "day_tasks": day_tasks,
        "instance": instance,
    }
    return render(request, "schedules/edit_day.html", context)


def _calc_duration(start, end):
    start = datetime.datetime.strptime(start, "%H:%M")
    end = datetime.datetime.strptime(end, "%H:%M")
    duration = str(end - start)
    return duration
