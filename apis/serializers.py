from rest_framework import serializers
from .models import *

class BSEserializer(serializers.ModelSerializer):
    class Meta:
        model = BSE
        fields = '__all__'

class NSEserializer(serializers.ModelSerializer):
    class Meta:
        model = NSE
        fields = '__all__'

class AshokSerializer(serializers.ModelSerializer):
    class Meta:
        model = AshokLeyland
        fields = '__all__'

class CiplaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cipla
        fields = '__all__'

class EicherSerializer(serializers.ModelSerializer):
    class Meta:
        model = EicherMotors
        fields = '__all__'

class RelianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reliance
        fields = '__all__'

class TatasteelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TataSteel
        fields = '__all__'