from django.shortcuts import render


# Create your views here.
def index(req):
    return render(req, 'signin.html',)


def theme(req):
    return render(req, 'theme.html',)


def login(req):
    return render(req, 'login.html',)


def signout(req):
    return render(req, 'signout.html')
