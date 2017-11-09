from django.contrib import admin

from .models import TrucksInfo, CurrentTrucksLoad


admin.site.register(TrucksInfo)
admin.site.register(CurrentTrucksLoad)
