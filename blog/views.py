from django.shortcuts import render, redirect,get_object_or_404, HttpResponseRedirect
from .models import PostModel
from .forms import PostModelForm , PostUpdateForm ,CommentForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
@login_required
def index(request):
    # Retrieve only approved posts
    posts = PostModel.objects.filter(approved=True).order_by('-date_created')

    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            # New posts are not approved by default
            instance.approved = False
            instance.save()
            return redirect('blog-index')
    else:
        form = PostModelForm()

    context = {
        'posts': posts,
        'form': form
    }

    return render(request, 'blog/index.html', context)


def like_post(request, post_id):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to like a post.")
        return HttpResponseRedirect(reverse('blog-index'))

    post = get_object_or_404(PostModel, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        post.dislikes.remove(request.user)  # Ensure a user cannot like and dislike at the same time
    return HttpResponseRedirect(reverse('blog-index'))

def dislike_post(request, post_id):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to dislike a post.")
        return HttpResponseRedirect(reverse('blog-index'))

    post = get_object_or_404(PostModel, id=post_id)
    if request.user in post.dislikes.all():
        post.dislikes.remove(request.user)
    else:
        post.dislikes.add(request.user)
        post.likes.remove(request.user)  # Ensure a user cannot like and dislike at the same time
    return HttpResponseRedirect(reverse('blog-index'))

@login_required
def post_detail(request,pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
           instance= c_form.save(commit=False)
           instance.user = request.user
           instance.post = post
           instance.save()
           return redirect('blog-post-detail', pk=post.id)
    else:
        c_form = CommentForm()

        
    
        
    
    context = {
        'post': post,
        'c_form': c_form,

    }
    return render(request, 'blog/post_detail.html', context)

@login_required
def post_edit(request, pk):
    post = get_object_or_404(PostModel, id=pk)  # Use get_object_or_404 for better error handling
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, request.FILES, instance=post)  # Pass request.FILES
        if form.is_valid():
            form.save()
            return redirect('blog-post-detail', pk=post.id)
    else:
        form = PostUpdateForm(instance=post)
    
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'blog/post_edit.html', context)

@login_required
def post_delete(request, pk):
    post = PostModel.objects.get( id=pk)

    
    if request.method == 'POST':
        post.delete()
        return redirect('blog-index')  # Make sure 'blog-home' exists in your urls.py
    
    context = {
        'post': post,
    }
    return render(request, 'blog/post_delete.html', context)

def home(request):
    posts =PostModel.objects.select_related('author').all()  # Make sure 'author' is properly related
    return render(request, 'home.html', {'posts': posts})

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Comment
