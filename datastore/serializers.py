from rest_framework import serializers
from .models import StkEk, Insurance, Vignette, Mileage

class StkEkSerializer(serializers.ModelSerializer):
    class Meta:
        model = StkEk
        fields = ['inspection_id', 'vin', 'inspection_date', 'valid_to', 'service_address', 'protocol', 'result']

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = ['insurance_date', 'valid_to', 'insurance_company', 'policy_number']


class VignetteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vignette
        fields = ['type', 'price', 'valid_from', 'valid_to']

class MileageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mileage
        fields = '__all__'
