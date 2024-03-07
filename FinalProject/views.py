from django.shortcuts import render, redirect
from .models import User, critic, movie
from .forms import criticForm #اینها با توجه به اسامی ای که در بخش های مدل و غیره می زنیم زیاد و کم میشن

# Create your views here.
def createc(request): #createc means create critic/ so createm means create movie
    pass



def retrievec(request, id):
    pass


def updatec(request):
    pass


def deletec(request, id):
    pass


def createm(request):# 
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


def retrievem(request, id):
    pass


def updatem(request, id):
    pass


def deletem(request, id):#
    k = Movie.objects.get(id=id)
    if request.user.id == k.creator.id:
        k.delete()
        return redirect('delete-movie')#دوباره اگه خواست پاک کنه

def usersignup(request):
    pass


def userlogin(request):
    pass


def userlogout(request):
    pass


