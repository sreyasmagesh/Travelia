from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def newhome(request):
    return render(request,'newhome.html')

def home(request):
    return render(request,'home.html')
def popular(request):
    return render(request,'popular.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def log(request):
    return render(request,'login.html')
def explore(request):
    return render(request,'explore.html')
def beaches(request):
    return render(request,'beaches.html')
def mountains(request):
    return render(request,'mountains.html')
def forest(request):
    return render(request,'forest.html')
def sellerlogin(request):
    return render(request,'sellerlogin.html')
def hotels(request):
    return render(request,'hotels.html')
def paramounthotel(request):
    return render(request,'paramounthotel.html')