import requests
from datetime import datetime

from django.http import HttpResponse


def datetime_now(request):
    """
    Return the date and time locally on the server.
    """
    try:
        now = datetime.now()
        response = '{' + '"success": true, "timestamp": {}'.format(now) + '}'
        return HttpResponse(response, content_type='application/json')
    except Exception as exc:
        res_json = '{' + '"success": false, "error": "{}"'.format(exc) + '}'
        return HttpResponse(res_json, content_type='application/json')


def server_ip(request):

    """
    Return the public ip of this machine.
    """
    try:
        res = requests.get('https://api.my-ip.io/ip.json')
        return HttpResponse(res.text, content_type='application/json')
    except Exception as exc:
        res_json = '{' + '"success": false, "error": "{}"'.format(exc) + '}'
        return HttpResponse(res_json, content_type='application/json')
