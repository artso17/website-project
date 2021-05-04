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

skills = Skill.objects.all()
services = Service.objects.all()
portfolios = Portfolio.objects.all()
blogs = Blog.objects.all()


def home(request):
    myabout = About.objects.get(judul='About Me')
    birth = myabout.birthday
    datenow = datetime.date.today()
    dayage = datenow-birth
    age = dayage.days//365
    portfolio_by_published = portfolios.order_by('-published')
    blog_by_published = blogs.order_by('-published')
    new_portfolios = []
    for i in range(len(portfolio_by_published)):
        if i == 6:
            break
        new_portfolios.append(portfolio_by_published[i])

    new_blogs = []
    for i in range(len(blog_by_published)):
        if i == 6:
            break
        new_blogs.append(blog_by_published[i])

    contact = CreateModel(request.POST)

    pengirim = ''
    konteks = {
        'judul': 'home',
        'abouts': myabout,
        'skills': skills,
        'age': age,
        'services': services,
        'portfolios': new_portfolios,
        'blogs': new_blogs,
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


def PortfolioFilterView(request, myskill):
    portfolios = Portfolio.objects.filter(skill__judul=myskill)
    konteks = {
        'portfolios': portfolios,
    }
    return render(request, 'blog/index.html', konteks)


def PortfolioAllView(request):
    konteks = {
        'portfolios': portfolios,
    }
    return render(request, 'blog/index.html', konteks)
