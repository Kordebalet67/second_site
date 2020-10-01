from django.shortcuts import render
from .forms import *
import pymysql
# Create your views here.

from django.shortcuts import render


def landing(request):
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data

        print(data["first_name"])  # обращение к конкретному полю входящей формы с инфой
        new_form = form.save()

    return render(request, 'landing/landing.html', locals())


def home(request):
    return render(request, 'landing/home.html', locals())
