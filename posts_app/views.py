from django.shortcuts import render, redirect
from posts_app.models import Posts
from django.urls import reverse
from django.http import HttpResponseRedirect
from posts_app.forms import PostForm
from django.contrib import messages

def post_list(request):
    template_name = 'post-list.html'
    posts = Posts.objects.all()
    context = {
        'posts': posts
    }

    return render(request, template_name, context)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            #form = form.save(commit=False)
            form.save()

            messages.success(request, 'Post criado com sucesso')
            return HttpResponseRedirect(reverse('post-list'))
        else:
            return render(request, 'post-form.html', {"form": form})
    else:
        form = PostForm()
        return render(request, 'post-form.html', {"form": form})

def post_details(request, id):
    template_name = 'post-detail.html'
    post = Posts.objects.get(id=id)
    print(post)
    context = {
        'post': post
    }
    return render(request, template_name, context)