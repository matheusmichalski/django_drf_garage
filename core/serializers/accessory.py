from rest_framework.serializers import ModelSerializer

from core.models import Accessory


class AccessorySerializer(ModelSerializer):
    class Meta:
        model = Accessory
        fields = "__all__"
