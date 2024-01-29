from django.contrib import messages, auth
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# from lodapp.form import RegistrationForm
from lodapp import form
from lodapp.models import UserProfile


def home(request):
    return render(request, 'home-base.html')


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credientials")
    return render(request,"login.html")



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm = request.POST['con_password']
        if password == confirm:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exist")
            else:
                user = User.objects.create_user(username=username, password=password,)
                user.save();
                return redirect('lodapp:login')

        else:
            messages.info(request, "Password is not matched")
            return redirect('register')


    return render(request, "register.html")




def registration_form(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('success.html')
            except:
                pass

    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'registration_form.html', context)


class RegistrationForm():
    class Meta:
        model = UserProfile
        fields = '__all__'


def logout(request):
    auth.logout(request)
    return redirect('/')


def success(request):
    return render(request, 'success.html')
