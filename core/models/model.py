
from django.db import models


class VehicleModel(models.Model):
    name = models.CharField(max_length=80)
    brand = models.CharField(max_length=80, null=True, blank=True)
    category = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        brand = (self.brand or '').upper()
        name = self.name.upper()
        return f'({self.id}) {brand} {name}'.strip()
