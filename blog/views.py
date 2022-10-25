from django.shortcuts import render
from django.http import HttpResponse
from.models import Post
# Create your views here.

def index(request):
    
    db = Post.objects.all()
    context ={
        'title' :'Blog',
        'heading' : 'Blog',
        'subheading' : 'Postingan',
        'post' : db,
    }
    return render(request, 'blog/index.html',context)

def recent(request):
    return HttpResponse("Recent")

