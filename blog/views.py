from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone

from .models import Post
from .models import PostForm
from .models import EditForm


# Create your views here.

def index(request):
    latest_posts = Post.objects.order_by('-pub_date').filter(completed=False)[:10]
    latest_posts_completed = Post.objects.filter(completed=True)
    template = loader.get_template('blog/index.html')
    context = {
        'latest_posts': latest_posts,
        'latest_posts_completed': latest_posts_completed,
    }
    return HttpResponse(template.render(context, request))


def detail(request, id):
    latest_posts = Post.objects.order_by('-pub_date').filter(completed=False)[:10]
    latest_posts_completed = Post.objects.filter(completed=True)
    task_detail = get_object_or_404(Post, pk=id)
    initial_a = task_detail.pub_date.replace(microsecond=0)
    b = timezone.now().replace(microsecond=0)
    time_passed = b - initial_a

    template = loader.get_template('blog/detail.html')
    context = {
        'task_detail': task_detail,
        'latest_posts': latest_posts,
        'time_passed': time_passed,
        'latest_posts_completed': latest_posts_completed,
    }
    return HttpResponse(template.render(context, request))


def blog(request):
    return render(request, 'blog/blog.html')

def stats(request):
    template = loader.get_template('blog/test.html')
    return HttpResponse(template.render())

def new_task(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_task = form.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm()
        template = loader.get_template('blog/newtask.html')
        context = {
        'form': form
        }
        return HttpResponse(template.render(context, request))

def edit_task(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = EditForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('detail', id=post.id)
    else:
        form = EditForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})   