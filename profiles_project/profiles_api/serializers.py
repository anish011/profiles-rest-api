from rest_framework import serializers


class HelloSerilaizer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
