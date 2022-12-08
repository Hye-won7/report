from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Reviews

# Create your views here.

def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())
    #return HttpResponse('<h1>안녕하세요 김혜원입니다.</h1>')

def photo(request):
    template = loader.get_template("photo.html")
    return HttpResponse(template.render())

def review(request):
    r = Reviews.objects.all().values()
    return render(request, 'review.html', {'r' : r})

def add(request):
    return render(request, 'add.html')

def addrecord(request):
    name = request.POST['name']
    content = request.POST['content']
    r = Reviews(name=name, content=content)
    r.save()
    return redirect('review')

def delete(request, id):
    r = Reviews.objects.get(id=id)
    r.delete()
    return redirect('review')

def update(request, id):
    r = Reviews.objects.get(id=id)
    return render(request, 'update.html', {'r' : r})

def updaterecord(request, id) :
    r = Reviews.objects.get(id=id)
    r.name = request.POST['name']
    r.content = request.POST['content']
    r.save()
    return redirect('review')