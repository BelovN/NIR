from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from .forms import DistributionForm

import matplotlib.pyplot as plt
import io
import urllib
import base64


def format_date(date, time):
    return datetime.strptime(date + ' ' + time, '%d.%m.%Y %H:%M:%S')


def main_view(request):
    if request.GET.get('begin_date_0', None):
        begin_date = format_date(request.GET.get('begin_date_0'), request.GET.get('begin_date_1'))
        finish_date = format_date(request.GET.get('finish_date_0'), request.GET.get('finish_date_1'))
        station = request.GET.get('station', None)
        initial = {
                'station' : station,
                'begin_date': begin_date,
                'finish_date': finish_date,
        }
        form = DistributionForm(initial=initial)
        if form.is_valid():
            request.session['form_data'] = form.cleaned_data

    else:
        initial = request.session.get('form_data')
        if initial is None:
            initial = {
                'begin_date': datetime(year=2015, month=1, day=1,
                                       hour=0, minute=0, second=0, microsecond=0),
                'finish_date': datetime(year=2015, month=1, day=2,
                                        hour=0, minute=0, second=0, microsecond=0),
            }
        form = DistributionForm(initial=initial)



    plt.plot(range(10), range(10), "o")
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)

    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    context = dict()
    context['graph'] = uri
    context['form'] = form
    return render(request, 'distributions/main.html', context)
