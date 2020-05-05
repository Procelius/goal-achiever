from django import forms

from . import models


class TimePeriodForm(forms.ModelForm):
    class Meta:
        model = models.TimePeriod
        fields = [
            'start',
            'end',
            'task',
        ]
        widgets = {
            'start': forms.TimeInput(attrs={'id': 'start-time'}, format='%H:%M'),
            'end': forms.TimeInput(attrs={'id': 'end-time'}, format='%H:%M'),
            'task': forms.RadioSelect,
        }

    def __init__(self, user, *args, **kwargs):
        super(TimePeriodForm, self).__init__(*args, **kwargs)
        self.fields['task'].queryset = models.Task.objects.filter(user=user)


class DayScheduleForm(forms.ModelForm):
    class Meta:
        model = models.DaySchedule
        fields = [
            'name',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'id': 'day-schedule-name'}),
        }

    def __init__(self, user, *args, **kwargs):
        super(DayScheduleForm, self).__init__(*args, **kwargs)
