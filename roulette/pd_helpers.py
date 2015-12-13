__author__ = 'ghoranyi'

from django.conf import settings

import pygerduty
import simplejson

def get_pd_api_key():
    secret_file = settings.SECRET_FILE
    secret_data = simplejson.load(open(secret_file))
    return secret_data['pagerduty_api_key']

def get_pd_subdomain():
    secret_file = settings.SECRET_FILE
    secret_data = simplejson.load(open(secret_file))
    return secret_data['pagerduty_subdomain']

def get_pd_client():
    pd_client = pygerduty.PagerDuty(get_pd_subdomain(), get_pd_api_key())
    return pd_client

def get_pd_users():
    pd_client = get_pd_client()
    users = pd_client.users.list()
    response = {
        "users": []
    }
    for user in users:
        response['users'].append({
            "name": user.name,
            "id": user.id
        })
    return response
