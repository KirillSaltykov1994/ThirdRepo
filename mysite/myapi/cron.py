import cronjobs
from .models import Staff
import json
from urllib.request import urlopen
from rest_framework.response import Response


@cronjobs.register
def periodic_task():
    print('HI! I AM YOUR CRON TASK! LETS ROCK!')
    response = {}
    r = urlopen('https://random-data-api.com/api/cannabis/random_cannabis?size=10')
    r_status = r.getcode()
    if r_status == 200:
        data = json.loads(r.read())
        for c in data:
            new_record = Staff(id=c.get('id'), uid=c.get('uid'), strain=c.get('strain'),
                             cannabinoid_abbreviation=c.get('cannabinoid_abbreviation'),
                             cannabinoid=c.get('cannabinoid'), terpene=c.get('terpene'),
                             medical_use=c.get('medical_use'),
                             health_benefit=c.get('health_benefit'), category=c.get('category'), type=c.get('type'),
                             buzzword=c.get('buzzword'), brand=c.get('brand'))
            new_record.save()
        response['status'] = 200
        response['message'] = 'success'
        response['credentials'] = data
    else:
        response['status'] = r.status_code
    return Response(response)
