from rest_framework.viewsets import ModelViewSet

from core.models import Accessory
from core.serializers import AccessorySerializer


class AccessoryViewSet(ModelViewSet):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer
