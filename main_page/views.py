from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.utils import timezone

import requests


def index(request):

    context = {
        '': ''
    }
    return render(request, 'main_page/index.html', context)


def services(request):

    context = {
        '': ''
    }
    return render(request, 'main_page/services.html', context)


def about(request):

    context = {
        '': ''
    }
    return render(request, 'main_page/about.html', context)


def contact(request):

    '''
    recaptcha_response = request.POST.get('g-recaptcha-response')
    data = {
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
    }
    r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    result = r.json()
    '''

    context = {
        '': ''
    }
    return render(request, 'main_page/contact.html', context)
