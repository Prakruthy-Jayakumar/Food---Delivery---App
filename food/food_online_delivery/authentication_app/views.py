from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect
from authentication_app.forms import OrderNowForm
from food_app.models import Place, District, Order, Food


def login(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['your_pass']
        fetch_details = auth.authenticate(username = user_name, password = password)
        if fetch_details is not None:
            auth.login(request,fetch_details)
            return redirect('/authentication/ordernow')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return  render(request, 'login_page.html')

def register(request):
    if request.method == 'POST':
        username =  request.POST['username']
        first_name =  request.POST['firstname']
        last_name =  request.POST['lastname']
        email =  request.POST['email']
        password =  request.POST['pass']
        confirm_password =  request.POST['re_pass']
        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username is already taken")
                return redirect('registration')
            elif User.objects.filter(email = email).exists():
                messages.info(request, "Email is already taken")
                return redirect('registration')
            else:
                user = User.objects.create_user(username = username,
                                   first_name = first_name,
                                   last_name = last_name,
                                   email = email,
                                   password = password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')
    return  render(request, 'registration.html')


def load_cities(request):
    district_id = request.GET.get('district_id')
    places = Place.objects.filter(district_id=district_id)
    return render(request, 'load_places.html', {'places': places})




def order(request, total= 0):
    foods = Food.objects.all()
    form = OrderNowForm()
    print(request.method)
    if request.method == 'POST':
        print("This is post")
        form = OrderNowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/authentication/ordersucess')
    return render(request, 'order_now.html', {'form': form,'foods': foods})


def successOrder(request):
    return render(request, 'success.html')

def logout(request):
    auth.logout(request)
    return redirect('/')