from django.shortcuts import render,redirect
from django.http import HttpResponse

from photoalbum.settings import MEDIA_ROOT
from .models import Category,Photos

from django.conf import settings
import os


# Create your views here.

def gallery(req) : 
    # category = req.GET.get('category','None')
    # category = category[:len(category)]
    # # type = req.GET.get('type','-1')
    # categories = Category.objects.all()
    # photos = Photos.objects.all()
    
   
    # # data = {'category':category , 'img_type' : type}
    # # print(type)
    
    # if category != 'None' : 
    #     category = Category.objects.get(name=category)
    #     photos = Photos.objects.filter(category=category)
    # # if type != '-1' : 
    # #     photos = photos.filter(type=type)
    # categories = []
    # for photo in Photos.objects.all() : 
    #     categories.append(photo.category)
    # context = {'categories' : categories , 'photos' : photos }
    return render(req,'photos/gallery.html')


def add(req) : 
    categories = Category.objects.all()
    
    if req.method == 'POST' : 
        data = req.POST
        image = req.FILES.get('image')
        name = data['name']
        convert = data['convert']
        
        if data['category'] != 'none' : 
            category =  Category.objects.get(id=data['category']) 
        elif data['new_category'] != '' :
            category,created = Category.objects.get_or_create(name = data['new_category'])
        else : 
            category = None
        
       
        photo = Photos.objects.create(
            name = name ,
            category = category ,
            image = image , 
            type = convert
        )
        
        return redirect('gallery')
        
    context = {'categories' : categories}
    return render(req,'photos/add.html',context)

def photo(req,pk) : 
    photo = Photos.objects.get(id=pk)
    context = {'photo' : photo}
    print(photo.name)
    return render(req,'photos/photo.html',context)


def delete(req,pk) : 
    photo = Photos.objects.get(id=pk)
    print(photo.image)
    
    os.remove("static/images/"+str(photo.image))
    photo.delete()
    
    return redirect("gallery")

# def download(request,path) :
   