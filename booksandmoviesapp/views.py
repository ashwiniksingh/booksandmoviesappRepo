from django.shortcuts import get_object_or_404, render, redirect
from booksandmoviesapp.models import booksandmovies
from django.contrib import messages
# Create your views here.
def addView(request):
    return render(request,'booksandmoviesapp/add.html')

def store(request):
    booksandmoviesStore = booksandmovies()
    booksandmoviesStore.booksandmovies_name = request.POST.get('booksandmovies_name')
    booksandmoviesStore.booksandmovies_link = request.POST.get('booksandmovies_link')
    booksandmoviesStore.booksandmovies_remark = request.POST.get('booksandmovies_remark')
    booksandmoviesStore.save()
    messages.success(request, "Book/Movie Added Successfully!")
    return redirect('index')

def index(request):
    booksandmoviesItem = booksandmovies.objects.all()
    return render(request, 'booksandmoviesapp/index.html',{'booksandmoviesItem':booksandmoviesItem})

def viewBookorMovie(request,pk):
   bookormovie = booksandmovies.objects.get(id = pk)
   return render(request, 'booksandmoviesapp/view.html',{'bookormovie':bookormovie})

def deleteBookorMovie(request, pk):
    bookormovie = booksandmovies.objects.get(id = pk)
    bookormovie.delete()
    messages.success(request, "Book/Movie Deleted Successfully")
    return redirect('index')

def updateBookorMovie(request,pk):
    updateBookorMovie = booksandmovies.objects.get(id = pk)
    return render(request,'booksandmoviesapp/update.html',{'updateBookorMovie':updateBookorMovie})

def update(request,pk):
    booksandmoviesUpdate = booksandmovies.objects.get(id = pk)
    booksandmoviesUpdate.booksandmovies_name = request.POST.get('booksandmovies_name')
    booksandmoviesUpdate.booksandmovies_link = request.POST.get('booksandmovies_link')
    booksandmoviesUpdate.booksandmovies_remark = request.POST.get('booksandmovies_remark')
    booksandmoviesUpdate.save()
    messages.success(request, "Book/Movie Updated Successfully!")
    return redirect('index')

"""
def header(request):
    return render(request, 'static/header.html')
"""