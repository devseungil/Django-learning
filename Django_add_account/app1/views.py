from django.shortcuts import render, redirect
from .models import Article
from .forms import Articleform
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(req):
    articles = Article.objects.all()[::-1]
    context = {
        'articles' : articles,
    }
    return render(req, 'app1/index.html',context)
@login_required
def create(req):
    if req.method == 'POST':
        form = Articleform(req.POST)
        if form.is_valid():
            article = form.save()
            return redirect('app1:detail', article.pk)
    else:
        form = Articleform()
    context = {
        'form' : form,
        'title' : 'CREATE'
    }
    return render(req,'app1/create.html', context)
@login_required
def detail(req, pk):
    article = Article.objects.get(pk =pk)
    context = {
        'article' : article
    }
    return render(req, 'app1/detail.html', context)

def update(req, pk):
    article = Article.objects.get(pk = pk)
    if req.method == 'POST':
        form = Articleform(req.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('app1:detail', article.pk)
    else:
        form = Articleform(instance=article)
    context = {
        'form' : form,
        'title' : 'UPDATE'
    }
    return render(req, 'app1/create.html', context)

def delete(req,pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('app1:index')

