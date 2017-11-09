from django.shortcuts import render
from django.db.models import F

from .models import ModelTruckInfo, CurrentTruckInfo


def current_info(request):
    form = request.POST
    trucks_info = CurrentTruckInfo.objects.all()
    truck_models = trucks_info.values('model_truck_info__truck_model').distinct()
    context = {"truck_models": truck_models}
    if form.get('send') and form.get('truck_model') != 'all':        
        truck_model = form.get('truck_model')
        context['trucks_info'] = trucks_info.filter(
                    model_truck_info__truck_model=truck_model
                ).annotate(over_load=F('current_load')*100/F('model_truck_info__carrying_capacity')-100)
    else:
        context['trucks_info'] = trucks_info.annotate(over_load=F('current_load')*100/F('model_truck_info__carrying_capacity')-100)
    return render(request, 'dispecer/current_info.html', context)
# a = CurrentTruckInfo.objects.annotate(over_load=F('current_load')*100/F('model_truck_info__carrying_capacity')-100)
