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
            'description': forms.TextInput(attrs={'id': 'goal-description'}),
            'tasks': forms.CheckboxSelectMultiple,
            'restrictions': forms.CheckboxSelectMultiple,
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = [
            'name',
            'description'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'id': 'task-name'}),
            'description': forms.TextInput(attrs={'id': 'task-description'}),
        }


class RestrictionForm(forms.ModelForm):
    class Meta:
        model = models.Restriction
        fields = [
            'name',
            'description'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'id': 'restriction-name'}),
            'description': forms.TextInput(attrs={'id': 'restriction-description'}),
        }
