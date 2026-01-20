from rest_framework import serializers
from .models import Device


class DeviceSerializer(serializers.ModelSerializer):
    worked_days = serializers.SerializerMethodField()
    display_name = serializers.SerializerMethodField()

    class Meta:
        model = Device
        fields = [
            'id',
            'name',
            'model',
            'serial_number',
            'start_date',
            'worked_days',
            'display_name',
            'manual',
        ]

    def get_worked_days(self, obj):
        return obj.worked_days

    def get_display_name(self, obj):
        return obj.display_name()