from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime


STATIONS = [
    ('ABD', 'ABD'),
    ('ABC', 'ABC'),
]


class DistributionForm(forms.Form):
    station = forms.ChoiceField(label='Станция', choices=STATIONS, required=True)
    begin_date = forms.DateTimeField(label='Начало', required=True, widget=AdminSplitDateTime())
    finish_date = forms.DateTimeField(label='Конец', required=True, widget=AdminSplitDateTime())
