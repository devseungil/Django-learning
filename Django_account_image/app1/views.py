from django.shortcuts import render, redirect
from .models import Article
from .forms import Articleform
from django.views.decorators.http import require_http_methods, require_POST, require_safe
#비로그인 입구컷
from django.contrib.auth.decorators import login_required

# Create yor views here.

def index(req):
    articles = Article.objects.all()[::-1]
    context = {
        'articles' : articles,
    }
    return render(req, 'app1/index.html', context)

# def new(req):
#     return render(req, 'app1/new.html')
@login_required
@require_http_methods(['GET', 'POST'])
def create(req):
    if req.method == 'POST':
        form = Articleform(req.POST, req.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('app1:detail', article.pk)
    else:
        form = Articleform()
    context = {
        'form' : form,
        'title' : 'CREATE'
    }
    return render(req, 'app1/create.html', context)
    # title = req.POST.get('title')
    # content = req.POST.get('content')

    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()
    
    # return redirect('app1:index')
@login_required    
@require_safe
def detail(req,pk):
    article = Article.objects.get(pk = pk)
    context = {
        'article' : article
    }
    return render(req, 'app1/detail.html', context)


def delete(request,pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk = pk)
        article.delete()
    return redirect('app1:index')

# def edit(req,pk):
#     article = Article.objects.get(pk = pk)
#     context = {
#         'article' : article
#     }
#     return render(req, 'app1/edit.html', context)

def update(req,pk):
    article = Article.objects.get(pk=pk)
    if req.method == 'POST':
        form = Articleform(req.POST,req.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('app1:detail', article.pk)
    else:
        form = Articleform(instance=article)
    context = {
        'form' : form ,
        'title' : 'UPDATE',
       
    }
    return render(req, 'app1/update.html', context)
    # article = Article.objects.get(pk = pk)
    # title = req.POST.get('title')
    # content = req.POST.get('content')

    # article.title = title
    # article.content = content
    # article.save()
    # return redirect('app1:detail', article.pk)


