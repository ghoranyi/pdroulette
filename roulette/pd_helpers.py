__author__ = 'ghoranyi'

from django.conf import settings

import pygerduty
import simplejson
import time


def get_pd_api_key():
    secret_file = settings.SECRET_FILE
    secret_data = simplejson.load(open(secret_file))
    return secret_data['pagerduty_api_key']


def get_pd_subdomain():
    secret_file = settings.SECRET_FILE
    secret_data = simplejson.load(open(secret_file))
    return secret_data['pagerduty_subdomain']


def get_pd_service_key():
    secret_file = settings.SECRET_FILE
    secret_data = simplejson.load(open(secret_file))
    return secret_data['pagerduty_service_key']


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


def create_incident():
    pd_client = get_pd_client()
    incident_key = pd_client.trigger_incident(
        service_key=get_pd_service_key(),
        description='You are the chosen one!',
    )
    return incident_key


def reassign_incident(incident_key, user_id):
    pd_client = get_pd_client()
    incident = next(pd_client.incidents.list(incident_key=incident_key))
    print("Reassigning {incident} to {user}".format(incident=incident_key, user=user_id))
    incident.reassign([user_id], 'PV133SN')


def create_incident_and_reassign(user_id):
    incident_key = create_incident()
    print("New incident triggered: {key}".format(key=incident_key))
    time.sleep(5)
    reassign_incident(incident_key, user_id)