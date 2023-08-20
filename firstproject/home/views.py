from.models import Product
from django.shortcuts import get_object_or_404, render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.decorators import login_required
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from math import ceil

# Create your views here.
@login_required(login_url='login2')

def index(request):
    # print(request.user)
    products= Product.objects.all()
    print(products)
    n=len(products)
    nslides=n//4 + ceil((n/4)-(n//4))
    params={ 'no_of_slides':nslides,'range':range(nslides),'product':products}
    
    if request.user.is_anonymous:
        return redirect("/login2") 
    return render(request, 'index.html',params)

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/home")

        else:
            # No backend authenticated the credentials
            return render(request, 'login2.html')

    return render(request, 'login2.html')

# def SignupPage(request):
#     if request.method=='POST':
#         uname=request.POST.get('username')
#         email=request.POST.get('email')
#         pass1=request.POST.get('password1')
#         pass2=request.POST.get('password2')
        
#         print(uname,email,pass1,pass2)

#         if pass1!=pass2:
#             return HttpResponse("Your password and confrom password are not Same!!")
#         else:

#             my_user=User.objects.create_user(uname,email,pass1)
#             my_user.save()
#             return redirect('login2')
   
   


#     return render (request,'signup.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!!")
        else:
            existing_user = User.objects.filter(username=uname).exists()
            if existing_user:
                messages.error(request, "User with this username already exists.")
                return redirect('signup')  # Redirect back to the signup page
            else:
                my_user = User.objects.create_user(uname, email, pass1)
                my_user.save()
                messages.success(request, "Account created successfully!")
                return redirect('login2')

    return render(request, 'signup.html')


# def signup(request):
#     # return HttpResponse("This is services page")
#      return render(request,'signup.html')

def logoutUser(request):
    logout(request)
    return redirect("/login2")


def about(request):
    # return HttpResponse("This is about page")
    if request.user.is_anonymous:
        return redirect("/login2") 
    return render(request, 'about.html')
def services(request):
    # return HttpResponse("This is services page")
    if request.user.is_anonymous:
        return redirect("/login2") 
    return render(request, 'services.html')
 
def household(request):
    # return HttpResponse("This is services page")
    products= Product.objects.all()
    print(products)
    n=len(products)
    nslides=n//4 + ceil((n/4)-(n//4))
    params={ 'no_of_slides':nslides,'range':range(nslides),'product':products}
    
    if request.user.is_anonymous:
        return redirect("/login2") 
    return render(request, 'household.html',params)

    if request.user.is_anonymous:
        return redirect("/login2") 
    return render(request, 'household.html')
 
def electronics(request):
    # return HttpResponse("This is services page")
    products= Product.objects.all()
    print(products)
    n=len(products)
    nslides=n//4 + ceil((n/4)-(n//4))
    params={ 'no_of_slides':nslides,'range':range(nslides),'product':products}
    
    if request.user.is_anonymous:
        return redirect("/login2") 
    return render(request, 'electronics.html',params)

    if request.user.is_anonymous:
        return redirect("/login2") 
    return render(request, 'electronics.html')

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact= Contact(name=name, email=email, phone=phone, desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your Message Has Been Sent!")
        
    # return HttpResponse("This is contact page")
    if request.user.is_anonymous:
        return redirect("/login2") 
    return render(request, 'contact.html')


def checkout(request):
    # return HttpResponse("This is about page")
    if request.user.is_anonymous:
        return redirect("/login2") 
    return render(request, 'checkout.html')

def tracker(request):
    if request.user.is_anonymous:
        return redirect("/login2") 
    return render(request, 'tracker.html')

def productview(request,product_id):
    #fetch the product using the id
    # product = get_object_or_404(Product, id=product_id)
    product= Product.objects.filter(id=product_id)
   
    
    return render(request, 'productview.html',{'product':product[0]})

def search(request):
    if request.user.is_anonymous:
        return redirect("/login2") 
    return render(request, 'search.html')