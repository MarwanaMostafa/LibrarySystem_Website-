from django.db.models.query import QuerySet
from django.http import request
from django.shortcuts import redirect, render
from .models import Book, Borrow
from django.contrib.auth.decorators import login_required
from .filters import SetOfFilters
from .forms import BorrowForm
from django.contrib.auth.models import User
from django import forms

# Create your views here.

@login_required
def books(request):
    bk = Book.objects.all()
    myFilter = SetOfFilters(request.GET, queryset=bk)
    bk = myFilter.qs
    return render(request, 'pages/Home.html', {'bok1':str(bk.count()), 'bok2':bk, 'myFilter':myFilter})

@login_required
def borrowing(request):
    initial = {}
    if request.user.is_authenticated:
        initial.update({'name':request.user})
    momo = BorrowForm(initial=initial)
    momo.fields['name'].widget = forms.HiddenInput()
    if request.method == 'POST':
        momo = BorrowForm(request.POST)
        if momo.is_valid():
            momo.save()
            return redirect('profile')
    return render(request, 'books/borrowbook.html', {'momo': momo})

@login_required
def extendPeriod(request, pk):
    borrow  = Borrow.objects.get(id = pk)
    momo = BorrowForm(instance=borrow)
    if request.method == 'POST':
        momo = BorrowForm(request.POST, instance=borrow)
        if momo.is_valid():
            momo.save()
            return redirect('profile')
    return render(request, 'books/borrowbook.html', {'momo': momo})

@login_required
def delete(request, pk):
    borrow  = Borrow.objects.get(id = pk)

    if request.method == 'POST':
        borrow.delete()
        return redirect('profile')
    return render(request, 'pages/delete.html', {'delete': borrow})
