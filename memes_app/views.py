from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.utils import timezone

from .models import Meme


def index(request):

    # write a query to return 5 questions and the most answered choice
    # add another file with sql queries
    # remember about SQL injection
    context = {
        'my_context': 'FIRST MEME URL'
    }
    return render(request, 'memes_app/index.html', context)
