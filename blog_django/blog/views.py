from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all() # თითოეული key შეესაბამება database ში შეყვანილ მოდულს სათითაოდ
    }
    return render(request, 'blog/home.html',context) # context კი გადაეცემა Templates

def about(request):
    return render(request, 'blog/about.html', { 'title':'About' })