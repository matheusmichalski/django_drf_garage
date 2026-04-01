
from django.db import models

from .accessory import Accessory
from .color import Color
from .model import VehicleModel


class Vehicle(models.Model):
    year = models.IntegerField(default=0, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    model = models.ForeignKey(VehicleModel, on_delete=models.PROTECT, related_name='vehicles')
    color = models.ForeignKey(Color, on_delete=models.PROTECT, related_name='vehicles')
    accessories = models.ManyToManyField(Accessory, related_name='vehicles', blank=True)

    def __str__(self):
        return f'({self.id}) {self.model} {self.color} {self.year}'
