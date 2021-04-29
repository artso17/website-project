from django.shortcuts import render
from .forms import CreateModel
from django.core.mail import send_mail
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

    if request.method == 'POST':
        if contact.is_valid():
            subject = request.POST.get('subject')
            pengirim = request.POST.get('pengirim')
            email = request.POST.get('email')
            deskripsi = request.POST.get('deskripsi')
            '''
            Contact.objects.create(
                subject=subject,
                pengirim=pengirim,
                email=email,
                deskripsi=deskripsi,
            )
            '''
            send_mail(
                f'Dari {pengirim} tentang {subject}',
                deskripsi,
                email,
                ['defuse805@gmail.com'],
            )

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
    return render(request, 'index.html', konteks)
