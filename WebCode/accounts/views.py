from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, userUpdateForm
from django.contrib.auth.decorators import login_required
from books.models import Borrow

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'pages/signup.html', {'form': form})
      

@login_required
def profile(requset):
    mybooks = Borrow.objects.all()
    return render(requset, 'pages/profile.html', {'mybooks': mybooks})

@login_required
def editprofile(request):
    if request.method == 'POST':
        user_form = userUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile')
    else:
        user_form = userUpdateForm(instance=request.user)
    return render(request, 'pages/editprofile.html', {'user_form':user_form})