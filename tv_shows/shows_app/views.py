from django.shortcuts import render, redirect
from .models import *

def index(request):
    return redirect('/shows')

def new(request):
    return render(request, 'new.html')

def shows(request):
    context={
        'all_shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)

def create(request):
    if request.method == 'POST':
        Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
        return redirect('/shows')
    return redirect('/shows/new')

def one_show(request, id):
    context={
        'viewed_show': Show.objects.get(id=id)
    }
    
    return render(request, 'one_show.html', context)


def edit_show(request, id):
    context={
        'edit_show': Show.objects.get(id=id),
        # "date": str(Show.objects.get(id=id).release_date)
    }
    
    return render(request, 'edit_show.html', context)


def update(request, id):
    if request.method == 'POST':
        str_id=str(id)
        edit_show=Show.objects.get(id=id)
        edit_show.title=request.POST['title']
        edit_show.network=request.POST['network']
        edit_show.release_date=request.POST['release_date']
        edit_show.description=request.POST['description']
        edit_show.save()
        
        return redirect(f'/shows/{str_id}')
        
    return redirect('/')

def destroy(request, id):
    Show.objects.get(id=id).delete()
    return redirect('/shows')