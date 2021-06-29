from rest_framework import serializers
from .models import ListAll


class ApiListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListAll
        fields = '__all__'
