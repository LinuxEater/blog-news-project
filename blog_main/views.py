from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Blog, Category

def home(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        }
    return render(request, 'home.html', context)