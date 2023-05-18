from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def index(req):
    # articles = Article.objects.all()

    # articles = Article.objects.order_by('-pk')
    # articles = Article.objects.order_by('-id')
    # db에서 내림차순으로 가져와 화면에 출력

    articles = Article.objects.all()[::-1]
    #전체조회해서 파이썬문법으로 내림차순변경해서 출력
    context = {
        'articles' : articles
    }
    return render(req,'app1/index.html',context)

# def new(req):
#     form = ArticleForm()
#     context = {
#         'form' : form
#     }
#     return render(req, 'app1/new.html',context)

def creat(request):
  if request.method == 'POST':
    form = ArticleForm(request.POST)
    if form.is_valid():
    
    #   form.save()
    #   return redirect('articles:detail', form.pk)
      # 1번방법
    
      article = form.save()
      return redirect('app1:detail', article.pk)
      # 2번방법
  else :
    form = ArticleForm() #빈 타이틀, 빈컨텐츠 만들어서 폼양식 화면에 보여준다 이뜻
    
  context = {
    'form' : form
  }
  return render(request, 'app1/creat.html', context)


# def creat(req):
#     form = ArticleForm(req.POST)
#     if form.is_valid():
#         # form.save()
#         # return redirect('app1:detail', form.pk)
#         article = form.save()
#         return redirect('app1:detail', article.pk)
#     return redirect('app1:new')    


#     # title = req.POST.get('title')
#     # content = req.POST.get('content')

#     # article = Article()
#     # article.title = title
#     # article.content = content
#     # article.save()
#     # return redirect('app1:detail', article.pk)

#     # articles = Article.objects.all()[::-1]
#     # context = {
#     #     'articles' : articles
#     # }
#     # return render(req, 'app1/index.html',context)
#     # return redirect('app1:index')

def detail(req,pk):
    article = Article.objects.get(pk=pk)
    
    context = {
        'article' : article,
    }
    return render(req, 'app1/detail.html', context)

def delete(req,pk):
    article = Article.objects.get(pk = pk)
    article.delete()

    # return render(req, 'app1/index.html')
    return redirect('app1:index')

# def edit(req,pk):
#     article = Article.objects.get(pk = pk)

#     context = {
#         "article" : article
#     }
#     return render(req, 'app1/edit.html',context)

def update(req, pk):
    article = Article.objects.get(pk = pk)

    if req.method == 'POST':
        form = ArticleForm(req.POST, instance=article) 
        #req.POST(입력받은애)랑 instance(기존있는애)랑 매칭시킨다는 뜻
        if form.is_valid():
            form.save()
            return redirect('app1:detail', article.pk)
        # article.title = req.POST.get('title')
        # article.content = req.POST.get('content')
        # article.save()
    else:
        form = ArticleForm(instance=article)
    context = {
        'form' : form ,
        'article' : article
    }
    return render(req, 'app1/update.html',context)