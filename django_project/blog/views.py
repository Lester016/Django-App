from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Lester De Guzman',
        'title': 'A Blog Post',
        'content': 'lorem ipsum dolor',
        'date_posted': 'December 26, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'A Post',
        'content': 'lorem ipsum dolor',
        'date_posted': 'December 16, 2019'
    }
]

def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html')