from django.shortcuts import render
from .models import *


def homepage(request):
    return render(request,'homepage.html')


def blog(request):
    maqolalar = Maqola.objects.all()
    return render(request,'blog.html',{'maqolalar':maqolalar})


def about(request):
    return render(request,'about.html')

def maqola(request,son):
    post = Maqola.objects.get(id=son)
    rasmlar = Rasmlar.objects.filter(Maqola=post)
    return render(request,'maqola.html',{'m':post, 'rasmlar':rasmlar})





































#
# from django.shortcuts import render
# from django.views.generic import ListView
# from .models import Maqola ,Rasmlar
#
# # Create your views here.
# class BlogListView(ListView):
#     model = Maqola
#     template_name = 'home.html'
#
#
#





