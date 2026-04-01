from rest_framework.serializers import ModelSerializer

from core.models import VehicleModel


class VehicleModelSerializer(ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = '__all__'
