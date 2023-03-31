from rest_framework import serializers
from rest_api.models import Record

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['id', 'date', 'lat', 'lon', 'city', 'state','temperature']

