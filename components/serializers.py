from rest_framework import serializers
from .models import Component, Chasis

from users.serializers import UsersSerializer


class ChasisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chasis
        fields = '__all__'


class ComponentsSerializer(serializers.ModelSerializer):
    submitter = UsersSerializer(read_only=True)
    chasis = ChasisSerializer(read_only=True)

    class Meta:
        model = Component
        fields = ('name', 'submitter', 'chasis')
