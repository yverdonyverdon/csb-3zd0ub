from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages 
from .models import *
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login as dj_login,logout

# Create your views here.


def indexview(request):
    return render(request,'index.html')

def register_as_service_provider(request):
    return render(request,'register_as_provider.html')

def signup(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')


        if len(username)>10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('/')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('/')
                    
        if (password != password2):
            messages.error(request, " Passwords do not match")
            return redirect('/')

        myuser = User.objects.create_user(username,email,password)
        myuser.first_name= firstname
        myuser.last_name= lastname
        myuser.save()

        instance = Signup(firstname=firstname,lastname=lastname,username=username,email=email,phoneno=phoneno,password=password)
        instance.save()

        group = Group.objects.get(name="Normal users")
        group.user_set.add(myuser)

        print("All data saved")
        messages.success(request,'You have registered successfully')
        return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST['loginusername']
        password = request.POST['loginpassword']

    user = authenticate(username = username,password=password)

    if user is not None:
        dj_login(request,user)
        messages.success(request,"Successfully Logged In")
        return redirect('/')
    
    else:
            messages.error(request,"Invalid LogIn details,please try again")
            return redirect('/')
            
def book(request):
    return render(request,'book.html')

def handlelogout(request):
    logout(request)
    messages.success(request,"SuccessFully Logged Out")
    return redirect('/')