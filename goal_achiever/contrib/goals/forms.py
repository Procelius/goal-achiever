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
