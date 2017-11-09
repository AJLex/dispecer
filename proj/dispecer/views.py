from django.shortcuts import render
from django.db.models import F

from .models import CurrentTrucksLoad


def current_info(request):
    form = request.POST
    trucks = CurrentTrucksLoad.objects.annotate(
        over_load=(F('current_load')-F('trucks_info__carrying_capacity'))*100/F('trucks_info__carrying_capacity'))
    truck_models = trucks.values('trucks_info__truck_model').distinct()
    context = {"truck_models": truck_models}
    if form.get('send') and form.get('truck_model') != 'all':
        context['trucks_info'] = trucks.filter(
            trucks_info__truck_model=form.get('truck_model'))
    else:
        context['trucks_info'] = trucks
    return render(request, 'dispecer/current_info.html', context)
