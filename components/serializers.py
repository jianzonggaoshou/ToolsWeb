from rest_framework import serializers
from .models import Component, Chasis

from users.serializers import UsersSerializer


class ChasisSerializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField()

    class Meta:
        model = Chasis
        fields = '__all__'

    def get_members(self, obj):
        pass


class ComponentsSerializer(serializers.ModelSerializer):
    submitter = UsersSerializer(read_only=True)
    chasis = ChasisSerializer(read_only=True)
    members = serializers.SerializerMethodField()

    class Meta:
        model = Component
        fields = ('name', 'submitter', 'chasis', 'members')

    def get_members(self, obj):
        return 'men213123123'

    def to_representation(self, obj):
        ret = {
            "name": obj.name,
            "members@.id": obj.submitter.username
        }
        return ret
