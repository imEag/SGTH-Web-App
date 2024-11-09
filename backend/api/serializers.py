from rest_framework import serializers
from .models import Professional, Device


class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = ['id', 'document', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name', 'brand', 'area', 'serial', 'responsible', 'image']
        read_only_fields = ['id']
