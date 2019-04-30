from rest_framework import serializers
from .models import AppsDatabase


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppsDatabase
        fields = (
            'id',
            'name',
            'launchYear',
            'serviceType',
            'businessModel',
            'description',
            'monitization',
            'tags',
        )
