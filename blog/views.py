from django.shortcuts import render,HttpResponse
from .models import Blog,Category
from rest_framework import viewsets
from .serializers import CategorySerializer,BlogSerializer
# Create your views here.

def home(request):
    blogs  = Blog.objects.all()
    category = Category.objects.all()
    return render(request,'index.html',{'blogs':blogs})

def blog_content(request,id):
    blog=Blog.objects.get(id=id)
    return render(request,'content.html',{'blog':blog})

def blog_form(request):
    if request.method == "POST":
        title= request.POST.get("")

    return render(request,'blog_form.html')


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
