from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    """
    Render the home page of the blog.
    """
    return render(request, 'home.html')