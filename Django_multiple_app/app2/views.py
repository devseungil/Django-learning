from django.shortcuts import render

# Create your views here.

def second(req):
    return render(req,'app2/second.html')
