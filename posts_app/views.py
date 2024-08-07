from django.shortcuts import render, get_object_or_404
from posts_app.models import Posts
from django.urls import reverse
from django.http import HttpResponseRedirect
from posts_app.forms import PostForm
from django.contrib import messages
from .forms import PostForm

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

def post_update(request, id):
    post = get_object_or_404(Posts, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()

        messages.success(request, 'Post atualizado com sucesso')
        return HttpResponseRedirect(reverse('post-detail', args=[post.id]))
    
    return render(request, 'post-form.html', {'form': form})