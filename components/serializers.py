from rest_framework import serializers
from .models import Component

from users.serializers import UsersSerializer


class ComponentsSerializer(serializers.ModelSerializer):
    submitter = UsersSerializer(read_only=True)

    class Meta:
        model = Component
        fields = ('name', 'submitter')
