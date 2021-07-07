from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
# Create your views here.
from .forms import LoginForm




def index(request):
    if request.user.is_authenticated:

        page = 'Index'
        data = {
            'title' : page
        }
        return render(request,'index.html', data)
    else:
        return redirect('/login/')

@csrf_protect
def login_page(request):

    if request.user.is_authenticated:
        return redirect("/")


    page = 'Login'
    data = {
        'title' : page
    }

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                error = "Login or password is incorrect"
                data['error'] = error
                data['form'] = form
                return render(request, 'login.html', data)
        else:
            error = "Login or password is incorrect"
            data['error'] = error
            data['form'] = form
            return render(request, 'login.html', data)
    else:
        form = LoginForm()
        data['form'] = form
    return render(request, 'login.html', data)



