from django.urls import path
from . import views
urlpatterns = [
   path('',views.newhome, name='newhome'),
   path('popular/',views.popular,name="popular"),
   path('about/',views.about,name="about"),
   path('contact/',views.contact,name="contact"),
   path('login/',views.log,name="login"),
   path('explore/',views.explore,name="explore"),
   path('beaches/',views.beaches,name='beaches'),
   path('mountains/',views.mountains,name='mountains'),
   path('forest/',views.forest,name='forest'),
   path('sellerlogin/',views.sellerlogin,name='sellerlogin'),
   path('hotels/',views.hotels,name='hotels'),
   path('paramounthotel/',views.paramounthotel,name='paramounthotel')
]