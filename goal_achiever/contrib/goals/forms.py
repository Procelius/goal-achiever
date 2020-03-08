from django import forms

from . import models


class GoalForm(forms.ModelForm):
    class Meta:
        model = models.Goal
        fields = [
            'name',
            'description',
            'tasks',
            'restrictions',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'id': 'goal-name'}),
            'description': forms.Textarea(attrs={'id': 'goal-description'}),
            'tasks': forms.CheckboxSelectMultiple,
            'restrictions': forms.CheckboxSelectMultiple,
        }

    def __init__(self, user, *args, **kwargs):
        super(GoalForm, self).__init__(*args, **kwargs)
        self.fields['tasks'].queryset = models.Task.objects.filter(user=user)
        self.fields['restrictions'].queryset = models.Restriction.objects.filter(user=user)


class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = [
            'name',
            'description'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'id': 'task-name'}),
            'description': forms.Textarea(attrs={'id': 'task-description'}),
        }

    def __init__(self, user, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)


class RestrictionForm(forms.ModelForm):
    class Meta:
        model = models.Restriction
        fields = [
            'name',
            'description'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'id': 'restriction-name'}),
            'description': forms.Textarea(attrs={'id': 'restriction-description'}),
        }

    def __init__(self, user, *args, **kwargs):
        super(RestrictionForm, self).__init__(*args, **kwargs)
