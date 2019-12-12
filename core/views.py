from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
# Create your views here.


def homes(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def portfolio(request):
    return render(request, "core/portfolio.html")


def contact(request):
    return render(request, "core/contact.html")


def post_list(request):
    # VARIABLE PARA GUARDAR QUERYSETS
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    #posts = Post.objects.all()
    return render(request, 'core/list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'core/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'core/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'core/post_edit.html', {'form': form})