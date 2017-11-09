from django.db import models


class TrucksInfo(models.Model):
    manufacturer = models.CharField(max_length=30, blank=True)
    truck_model = models.CharField(max_length=30)
    carrying_capacity = models.IntegerField()

    def __str__(self):
        return self.truck_model


class CurrentTrucksLoad(models.Model):
    trucks_info = models.ForeignKey(TrucksInfo, on_delete=models.CASCADE)
    board_number = models.CharField(max_length=30)
    current_load = models.IntegerField(default=0)

    def __str__(self):
        return self.board_number
