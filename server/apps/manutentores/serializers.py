from rest_framework import serializers
from .models import Manutentor

class ManutentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manutentor
        fields = '__all__'