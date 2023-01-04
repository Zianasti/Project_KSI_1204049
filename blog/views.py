from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from.models import Post
from.models import PostModel
from .forms import PostForm
# Create your views here.

def index(request):
    posts = PostModel.objects.all()
    db = Post.objects.all()
    context ={
        'page_title':'List Blog',
        'posts' : posts,
        'title' :'Blog',
        'heading' : 'Blog',
        'subheading' : 'Postingan',
        'post' : db,
    }
    return render(request, 'blog/index.html',context)

def create(request):
    post_form = PostForm(request.POST or None)

    if request.method == 'POST':
        if post_form.is_valid() :
            post_form.save()
        
        return HttpResponseRedirect("/blog/")

    context = {
        'page_title' : 'Create Post',
        'post_form' :post_form
    }

    return render(request, 'blog/create.html', context)

def recent(request):
    return HttpResponse("Recent")

def delete(request, delete_id):
    PostModel.objects.filter(id=delete_id).delete()
    return HttpResponseRedirect('/blog/')

def update(request, update_id):
    updt = PostForm.objects.get(id=update_id)
    data = {
        'author' : updt.author,
        'judul' : updt.judul,
        'body' : updt.body,
        'category' : updt.category,
    }

    postform = PostForm(request.Post or None, initial=data, instance=updt)

    if request.method == 'POST':
        if postform.is_valid():
            postform.save()
            return HttpResponseRedirect('/blog/')

    context = {
        'heading':'Update',
        'postform' : postform
    }
    return render(request, 'form.html', context)
