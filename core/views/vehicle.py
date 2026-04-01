from rest_framework.viewsets import ModelViewSet

from core.models import Vehicle
from core.serializers import VehicleSerializer


class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
