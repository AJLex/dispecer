from django.db import models


class ModelTruckInfo(models.Model):
    manufacturer = models.CharField(max_length=30)
    truck_model = models.CharField(max_length=30)
    carrying_capacity = models.IntegerField()


class CurrentTruckInfo(models.Model):
    model_truck_info = models.ForeignKey(ModelTruckInfo, on_delete=models.CASCADE)
    board_number = models.CharField(max_length=30)
    current_load = models.IntegerField()
