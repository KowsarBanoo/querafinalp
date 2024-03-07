from django.shortcuts import render, redirect, get_object_or_404 #404 baraye movie haei ke vojOod nadaran
from django.contrib.auth import login, logout, authenticate
from .models import User, critic, movie
from .forms import updatemForm, RegisterForm, LoginForm #اینها با توجه به اسامی ای که در بخش های مدل و غیره می زنیم زیاد و کم میشن

# Create your views here.
def createc(request): #createc means create critic/ so createm means create movie
    pass



def retrievec(request, id):
    pass


def updatec(request):
    pass


def deletec(request, id):
    pass


def createm(request):# arsalan
    if request.user.is_authenticated:# اگه لاگین بود
        if request.method == 'POST':#فرم رو پر کرده و فرستاده
            form = MovieForm(request.POST)
            if form.is_valid():
                user = User.objects.get(id=request.user.id)
                k = Movie.objects.create
                (
                    title = form.cleaned_data['title'],
                    text = form.cleaned_data['text']
                    creator = user
                )    
                return redirect('create', id = k.id)
            else:
                return render(request,'create_movie.html',{'form':form})
        else:#میخواد یه فرم پر کنه
            return render(request, 'create_movie.html', {'form':MovieForm()})
    else:
        return redirect("userlogin")


def retrievem(request, id): #masalan bezane retrieve,5 bayad betOone data ye film 5 ro bekhOone
    m= movie.objects.get (id=id)
    if request.user.id== m.creator.id:
        return render (request, 'read.html', {'object':m})


def updatem(request, id):
    if request.user.is_authenticated:
        if request.method=='GET':
            movie_id=request.GET.get('id')
            movie=get_object_or_404(movie,id=movie_id)
            return render(request,'movie.html', {'movie':movie}, {'form':updatemForm()})
    elif request.method =='POST':
    else:
        return redirect ("FinalProject:login")
    pass


def deletem(request, id):#arsalan
    k = Movie.objects.get(id=id)
    if request.user.id == k.creator.id:
        k.delete()
        return redirect('delete-movie')#دوباره اگه خواست پاک کنه


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


