from django.shortcuts import render
from rest_framework import viewsets

from .serializers import StaffSerializer
from .models import Staff
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from urllib.request import urlopen


class TestsViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all().order_by('uid')
    serializer_class = StaffSerializer


class GenerateStaffs(APIView):
    def get(self, request):
        response = {}
        r = urlopen('https://random-data-api.com/api/cannabis/random_cannabis?size=10')
        r_status = r.getcode()
        if r_status == 200:
            data = json.loads(r.read())
            print(data)
            for c in data:
                new_record = Staff(id=c.get('id'), uid=c.get('uid'), strain=c.get('strain'),
                                   cannabinoid_abbreviation=c.get('cannabinoid_abbreviation'),
                                   cannabinoid=c.get('cannabinoid'), terpene=c.get('terpene'),
                                   medical_use=c.get('medical_use'),
                                   health_benefit=c.get('health_benefit'), category=c.get('category'),
                                   type=c.get('type'),
                                   buzzword=c.get('buzzword'), brand=c.get('brand'))
                new_record.save()
            response['staffs'] = data
        else:
            response['message'] = 'error'
        return Response(response)
