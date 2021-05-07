from django.core.paginator import Paginator
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
    or_portfolios = Portfolio.objects.filter(
        slug=myskill).order_by('-published')
    skills = Skill.objects.all().exclude(slug=myskill)
    konteks = {
        'portfolios': or_portfolios,
        'skills': skills,
        'jumlah': len(or_portfolios)
    }
    if len(or_portfolios) > 12:
        paginator = Paginator(or_portfolios, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        konteks['portfolios'] = page_obj
        konteks['page_number'] = int(page_number)
        konteks['paginator'] = paginator
    return render(request, 'blog/portfolio_filter.html', konteks)


def PortfolioAllView(request):
    or_portfolios = portfolios.order_by('-published')
    skills = Skill.objects.all()
    konteks = {
        'skills': skills,
        'portfolios': or_portfolios,
        'jumlah': len(or_portfolios)

    }
    if len(or_portfolios) > 12:
        paginator = Paginator(or_portfolios, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        konteks['portfolios'] = page_obj
        konteks['page_number'] = int(page_number)
        konteks['paginator'] = paginator

    print(konteks)

    return render(request, 'blog/portfolio_all.html', konteks)


def PortfolioDetailView(request, detail_id):
    d_portfolio = Portfolio.objects.get(id=detail_id)
    skill = d_portfolio.slug
    skills = Skill.objects.all().exclude(slug=skill)
    oth_portfolio = Portfolio.objects.filter(slug=skill).exclude(id=detail_id)
    new_oth_portfolios = []
    for i in range(len(oth_portfolio)):
        new_oth_portfolios.append(oth_portfolio[i])
        if i == 6:
            break

    konteks = {
        'detail_portfolio': d_portfolio,
        'skills': skills,
        'oth_portfolios': new_oth_portfolios,

    }

    print(konteks)
    return render(request, 'blog/portfolio_detail.html', konteks)
