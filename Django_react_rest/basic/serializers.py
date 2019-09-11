from rest_framework import serializers
from basic.models import Basic


# Basic Serializer

class BasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basic
        fields = '__all__'
