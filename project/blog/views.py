from django.shortcuts import render, redirect
from .forms import CreateModel
from django.core.mail import send_mail, EmailMessage
import datetime

from .models import (
    About,
    Skill,
    Service,
    Portfolio,
    Blog,
    Contact,
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
    contact = CreateModel(request.POST)

    pengirim = ''
    konteks = {
        'judul': 'home',
        'abouts': myabout,
        'skills': skills,
        'age': age,
        'services': services,
        'portfolios': portfolios,
        'blogs': blogs,
        'contact': contact,

    }
    if request.method == 'POST':
        if contact.is_valid():
            subject = request.POST.get('subject')
            pengirim = request.POST.get('pengirim')
            email = request.POST.get('email')
            deskripsi = request.POST.get('deskripsi')
            Contact.objects.create(
                subject=subject,
                pengirim=pengirim,
                email=email,
                deskripsi=deskripsi,
            )

            konteks['pengirim'] = pengirim

    konteks['jumlah'] = {
        'portfolios': len(portfolios),
        'blogs': len(blogs),
    }
    return render(request, 'index.html', konteks)
