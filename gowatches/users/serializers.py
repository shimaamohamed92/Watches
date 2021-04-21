from django.contrib.auth.models import User, Group
from rest_framework import serializers
from gowatches.users.models import User


class UserSerializer(serializers.ModelSerializer):
    # queryset = User.objects.get(id=self.request.user.id)
    variant_list = serializers.SerializerMethodField()
    def get_variant_list(self, instance):
        variant_list = []
        a = instance.variant_list.get_queryset()
        for i in a:
            variant_list.append(i.name)
        return variant_list
    def validate_national_id(self, value):                                     
        if self.instance and value != self.instance.national_id:
            raise serializers.ValidationError("national_id is immutable once set.")
        return value  
    class Meta:
        model = User
        fields = ['name', 'first_name', 'email', 'last_name', 'phone', 'national_id', 'role','variant_list']
