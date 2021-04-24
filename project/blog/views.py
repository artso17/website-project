from django.shortcuts import render
import datetime

from .models import (
    About,
    Skill,
    Service,
    Portfolio,
    Blog,
    Contact
)
# Create your views here.


def home(request):
    myabout = About.objects.filter(judul='About Me').get()
    birth = myabout.birthday
    datenow = datetime.date.today()
    dayage = datenow-birth
    age = dayage.days//365

    skills = Skill.objects.all()
    services = Service.objects.all()
    portfolios = Portfolio.objects.all()
    blogs = Blog.objects.all()

    konteks = {
        'judul': 'home',
        'abouts': myabout,
        'skills': skills,
        'age': age,
        'services': services,
        'portfolios': portfolios,
        'blogs': blogs,

    }
    return render(request, 'index.html', konteks)
