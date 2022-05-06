from django.shortcuts import render

# Create your views here.
def adminlogin(request):
    return render(request,'adminlogin.html')
def adminhome(request):
    return render(request,'adminhome.html')
def customerbookings(request):
    return render(request,'customerbookings.html')
def todaybooking(request):
    return render(request,'todaybooking.html')

def hoteldetails(request):
    return render(request,'hoteldetails.html')
def hotelverification(request):
    return render(request,'hotelverification.html')