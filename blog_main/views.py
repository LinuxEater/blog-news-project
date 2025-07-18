from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Blog, Category
from assigmments.models import AboutUs, ContactsFunction

def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')
    try:
        about_us = AboutUs.objects.first()
        contacts = ContactsFunction.objects.all()
    except AboutUs.DoesNotExist:
        about_us = None
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'about_us': about_us,
        'contacts': contacts
        }
    return render(request, 'home.html', context)

