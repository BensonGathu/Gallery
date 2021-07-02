from django.shortcuts import render
from .models import Location,Category,Image
# Create your views here.

def welcome(request):
    images = Image.all_images()
    return render(request,'index.html',{"images":images})

def search(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request,"search.html",{"message":message,"images":searched_images})

    else:
        message = "You haven't searched for any category"
        return render(request,"search.html",{"message":message})