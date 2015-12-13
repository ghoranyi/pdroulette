from django.http.response import JsonResponse
from roulette.pd_helpers import get_pd_users

__author__ = 'ghoranyi'

def get_PD_users(request):
    return JsonResponse(get_pd_users())
