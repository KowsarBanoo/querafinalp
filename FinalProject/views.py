from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import User, critic, movie
from .forms import criticForm, RegisterForm, LoginForm #اینها با توجه به اسامی ای که در بخش های مدل و غیره می زنیم زیاد و کم میشن

# Create your views here.
def createc(request): #createc means create critic/ so createm means create movie
    pass



def retrievec(request, id):
    pass


def updatec(request):
    pass


def deletec(request, id):
    pass


def createm(request):
    pass


def retrievem(request, id):
    pass


def updatem(request, id):
    pass


def deletem(request, id):
    pass

def usersignup(request):
    if request.user.is_authenticated:
        return redirect('logout')
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                )
                login(request, user)
                return redirect ('createc')
            else:
                return render(request, 'signup.html', {'fom':form})
        else:
            return render(request, 'signup.html', {'form':RegisterForm()})
        
def userlogin(request):
    if request.user.is_authenticated:
        return redirect('logout')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password']
                )
                if user:
                    login(request, user)
                    return redirect('createc')
                else:
                    return render(request, 'login.html', {'form':form})
            else:
                return render(request, 'login.html', {'form':form})
        else:
            return render(request, 'login.html', {'form':LoginForm()})


def userlogout(request):
    logout(request)
    return redirect('login')


