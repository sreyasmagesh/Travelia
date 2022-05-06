from django.urls import path
from . import views
urlpatterns = [
   path('',views.sellerhome, name='sellerhome'),
   path('sellerlogin/',views.sellerlogin, name='sellerlogin'),
   path('sellerloginhome/',views.sellerloginhome, name='sellerloginhome'),
   path('sellersubmit/',views.sellersubmit, name='sellersubmit'),
   
]