# 404 baraye movie haei ke vojOod nadaran
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from .models import UserModel, FeedBack, Movie
# اینها با توجه به اسامی ای که در بخش های مدل و غیره می زنیم زیاد و کم میشن
from .forms import updatemForm, RegisterForm, LoginForm, MovieForm,UpdateFeedBackForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def createc(request):  # createc means create critic/ so createm means create movie
    if request.user.id .is_authenticated:
        if request.method == 'POST':
            form = UpdateFeedBackForm(request.POST)
            if form.is_valid():
                user = user.objects.get(id == request.user.id)
                naghd = FeedBack.objects.create(
                    title = form.cleaned_data['title'],
                    text = form.cleaned_data['text'],
                    creator = user
                )
                return redirect('FeedBack: read:{naghd.id}')
            else:
                return redirect(request,'build.html',{'form':form})
        else:
            return render(request, 'build.html', {'form':UpdateFeedBackForm})
    else:
        return render('FeeBack:login')


class RetrieveMyFeedBackView(LoginRequiredMixin, generic.DetailView):
    template_name = "detail-my-feedbacks.html"

    def get_queryset(self):
        return FeedBack.objects.filter(user=self.request.user)


class UpdateMyFeedBackView(LoginRequiredMixin, generic.UpdateView):
    template_name = "update_my_feedback_from.html"
    model = FeedBack
    fields = ['movie', 'personal_feedback']

    def get_queryset(self):
        return FeedBack.objects.filter(user=self.request.user)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)


def deletec(request, id):
    feed = FeedBack.object.get(id ==id) # it checks the given id . if that id was equal with user given , it allows user to delete the post.
    if request.user.id == feed:
        feed.delete()
        return redirect('FeedBack:create')
    return render(request,'delete.html',{'form':UpdateFeedBackForm()})


def createm(request):  # arsalan
    if request.user.is_authenticated:  # اگه لاگین بود
        if request.method == 'POST':  # فرم رو پر کرده و فرستاده
            form = MovieForm(request.POST)
            if form.is_valid():
                user = UserModel.objects.get(id=request.user.id)
                k = Movie.objects.create(
                    title=form.cleaned_data['title'],
                    text=form.cleaned_data['text'],
                    creator=user
                )
                return redirect('create', id=k.id)
            else:
                return render(request, 'create_movie.html', {'form': form})
        else:  # میخواد یه فرم پر کنه
            return render(request, 'create_movie.html', {'form': MovieForm()})
    else:
        return redirect("userlogin")


def retrievem(request, id): #masalan bezane retrieve,5 bayad betOone data ye movie ye 5 ro bekhOone
    movie= get_object_or_404 (Movie, id=id) #baz yabiye data haye obj mobie/ inja bayad modeli baraye mivie dashte bashim
    #if request.user.id== movie.creator.id:#inja faghat sazandeye movie mitOone behesh dastra30 dashte bashe 
    return render (request, 'read.html', {'object':movie}) #data ro neshOon mide behesh


def updatem(request, id): #id yani movie id
    if request.user.is_authenticated: #ke user log in bOode bashe pish az kar
        movie= get_object_or_404(Movie, id=id) #khob aval bayad data khOonde beshe va bad update rokh bd/ ag film ba id marbOote nabOod error 404 mide
        if request.method == 'GET': #baraye darkhaste data az yek manbae moshakhas (inja dar beyne movie ha mikhad be page shOon dastra30 peyda kone)
            form= updatemForm(instance=movie)
            return render (request, 'updatem.html', {'movie':movie, 'form':form}) #baraye inke detailm ro bbine va az tarighe form be rOozesh kone user
        elif request.method== 'POST': #in dastOor baraye send kardan data ha be ye manbae moshakha3/ masalan inja va3 update data haye delkhahe user, azash use kardam
            form= updatemForm(request.POST,instance=movie)
            if form.is_valid(): #ag data haye form valid bOod, data ha (dar khate bad) save mishan va user hedayat mishe be page detaile movie
                form.save()
                return redirect ('update-movie', id=id) #hedayata user be in page
            else: #yani ag not valid bOod data ye form
                return render(request, 'movie.html', {'movie':movie, 'form':form})#forme movie mojadad behesh barmigarde
    else: #ag user login nakarde khob bayad bargarde be page login
        return redirect("FinalProject:login") #bargasht be page login


def deletem(request, id):  # arsalan
    k = Movie.objects.get(id=id)
    if request.user.id == k.creator.id:
        k.delete()
        return redirect('delete-movie')  # دوباره اگه خواست پاک کنه


def usersignup(request):
    if request.user.is_authenticated:
        return redirect('userlogout')
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = UserModel.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                )
                login(request, user)
                return redirect('new-critique')
            else:
                return render(request, 'signup.html', {'form': form})
        else:
            return render(request, 'signup.html', {'form': RegisterForm()})


def userlogin(request):
    if request.user.is_authenticated:
        return redirect('userlogout')
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
                    return redirect('new-critique')
                else:
                    return render(request, 'login.html', {'form': form})
            else:
                return render(request, 'login.html', {'form': form})
        else:
            return render(request, 'login.html', {'form': LoginForm()})


def userlogout(request):
    logout(request)
    return redirect('userlogin')
