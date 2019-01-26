from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.utils import timezone
from django_ajax.decorators import ajax
from django.core.mail import EmailMessage

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


def valuation(request):
    context = {
        '': ''
    }
    return render(request, 'main_page/valuation.html', context)


@ajax
def contact_endpoint(request):

    email = EmailMessage(
        subject=request.POST['subject'],
        body="Message from "+request.POST['name']+"\n\n"+request.POST['message'],
        from_email='contact@dataguy.pl',
        to=['slusarczyk41@gmail.com'],
        reply_to=[request.POST['email']],
        headers={'Content-Type': 'text/plain'},
    )

    try:
        email.send()
        return True
    except ValueError:
        return False

@ajax
def download_cv_endpoint(request):

    return 'bla'