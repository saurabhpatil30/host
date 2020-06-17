from rest_framework import serializers
from seller.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Vehicle
        fields = ('id','name','brand','wheels')
