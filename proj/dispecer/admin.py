from django.contrib import admin

from .models import ModelTruckInfo, CurrentTruckInfo


admin.site.register(ModelTruckInfo)
admin.site.register(CurrentTruckInfo)
