__author__ = 'ghoranyi'
from roulette.pd_helpers import get_pd_users, create_incident_and_reassign

from django.http.response import JsonResponse
from django.shortcuts import render
import random


def get_PD_users(request):
    return JsonResponse(get_pd_users())


def index(request):
    return render(request, 'index.html', {})


def play(request):
    players = request.POST.getlist('players[]')
    print("Play request received with users: {users}".format(users=players))
    choice = random.choice(players)
    print("Choice: {choice}".format(choice=choice))
    create_incident_and_reassign(choice)
    return JsonResponse({
        "choice": choice
    })