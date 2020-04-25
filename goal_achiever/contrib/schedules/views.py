from django.shortcuts import render


def schedules(request):
    return render(request, "schedules/schedules.html", {})
