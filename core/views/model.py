from rest_framework.viewsets import ModelViewSet

from core.models import VehicleModel
from core.serializers import VehicleModelSerializer


class VehicleModelViewSet(ModelViewSet):
    queryset = VehicleModel.objects.all()
    serializer_class = VehicleModelSerializer
