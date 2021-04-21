from rest_framework.serializers import ModelSerializer
from .models import Watches, Varient
from gowatches.users.models import User
from rest_framework import serializers

class vairiantSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    image = serializers.CharField(read_only=True)
    model = serializers.CharField(read_only=True)

    class Meta:
        model = Varient
        fields = ("name","image", "model" )

class TrackSerializer(serializers.ModelSerializer):
    # waiting_list = serializers.SerializerMethodField()
    # def get_waiting_list(self, instance):
    #     names = []
    #     a = instance.waiting_list.get_queryset()
    #     for i in a:
    #         names.append(i.username)
    #     return names
    class Meta:
        model = Varient
        fields = ("name","image", "model")


class WatchesSerializer(serializers.ModelSerializer):
    varient = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Watches
        fields = ("name","image", "model", "varient", )

