from django.shortcuts import render


# Create your views here.
def index(req):
    return render(req, 'signin.html',)


def theme(req):
    return render(req, 'theme.html',)

