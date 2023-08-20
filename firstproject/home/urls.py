from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
   path('',views.loginUser,name='home'),
   path('signup',views.SignupPage,name='signup'),
   path('home',views.index,name='home'),
   path('about',views.about,name='about'),
   path('services',views.services,name='services'),
   path('household',views.household,name='household'),
   path('electronics',views.electronics,name='electronics'),
   path('contact',views.contact,name='contact'),
   # path('',views.index, name="home"),
    path('login2',views.loginUser,name="login2"),
    path('logout',views.logoutUser,name="logout"),
    path('checkout',views.checkout,name='checkout'),
    path('tracker',views.tracker,name='tracker'),
    path('products/<int:product_id>/',views.productview,name='product_details'), 
    path('search',views.search,name='search'),
#     path('signup',views.signup,name="signup")s
 ]

