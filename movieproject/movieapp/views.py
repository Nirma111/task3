from django.shortcuts import render,redirect
from .models import movie
from .forms import movieForm
from django.http import HttpResponse
# Create your views here.
def index(request):
    mov= movie.objects.all()
    return render(request,'index.html',{'list':mov})
def detail(request,movie_id):
    det=movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'idn':det})
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        mov=movie(name=name,desc=desc,year=year,img=img)
        mov.save()
    return render(request,'add.html')
def update(request, id):
    mo=movie.objects.get(id=id)
    form=movieForm(request.POST or None,request.FILES,instance=mo)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form, 'mov':mo})
def delete (request,id):
    if request.method=='POST':
        Mov=movie.objects.get(id=id)
        Mov.delete()
        return redirect('/')
    return render(request,'delete.html')