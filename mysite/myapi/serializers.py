from rest_framework import serializers

from .models import Staff

class StaffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff
        fields = ('id','uid','strain','cannabinoid_abbreviation',
                  'cannabinoid','terpene','medical_use','health_benefit','category','type','buzzword','brand')