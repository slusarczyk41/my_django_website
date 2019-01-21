from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.utils import timezone


def index(request):

    context = {
        'my_context': 'FIRST MEME URL'
    }
    return render(request, 'main_page/home.html', context)
