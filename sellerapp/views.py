from django.shortcuts import render


def sellerlogin(request):
    return render(request,'sellerlogin.html')
def sellerhome(request):
    return render(request,'sellerhome.html')
def sellerloginhome(request):
    return render(request,'sellerloginhome.html')
def sellersubmit(request):
    return render(request,'sellersubmit.html')