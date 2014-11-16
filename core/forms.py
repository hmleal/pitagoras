from django import forms
from core.models import PathWay


class PathWayForm(forms.Form):
    pathways = forms.MultipleChoiceField(
        choices=PathWay.objects.all().values_list('pk', 'name'),
        widget=forms.CheckboxSelectMultiple
    )

    def clean_pathways(self):
        return [int(path) for path in self.cleaned_data['pathways']]
