
from django.shortcuts import render, redirect, get_object_or_404, render

# Create your views here.
from django.contrib.auth.decorators import login_required

from .models import Post, BlogPersonal
from .forms import PostForm

@login_required
def agregar_post(request):
    blog = get_object_or_404(BlogPersonal, user=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.blog = blog
            post.save()
            return redirect('blog_list')  # Cambia a tu vista de lista de posts
    else:
        form = PostForm()
    return render(request, 'blog/agregar_post.html', {'form': form})


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, blog__user=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, blog__user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('blog_list')
    return render(request, 'blog/eliminar_post.html', {'post': post})



@login_required
def blog_list(request):
    
    posts = Post.objects.filter(blog__user=request.user)
    
    return render(request, 'blog/blog_list.html', {'posts': posts})




