from django.urls import path
from . import views
urlpatterns = [
   path('',views.adminlogin, name='adminlogin'),
   path('adminhome',views.adminhome, name='adminhome'),
   path('customerbookings',views.customerbookings, name='customerbookings'),
   path('hoteldetails',views.hoteldetails, name='hoteldetails'),
   path('todaybooking',views.todaybooking, name='todaybooking'),
   path('hotelverification',views.hotelverification, name='hotelverification'),

]