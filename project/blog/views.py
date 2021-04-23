from django.shortcuts import render

# Create your views here.


def home(request):
    konteks = {
        'judul': 'home',
    }
    return render(request, 'index.html', konteks)
