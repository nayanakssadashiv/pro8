from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def if_demo(request):
    login=True
    return render(request,"home.html",context={"login":login})
def else_demo(request):
    login=False
    return render(request,"else_demo.html",context={"login":login})
def for_demo(request):
    return render(request,"for_demo.html",context={"items":["apple","cat","dog"],"profile":{"name":"nayana","age":"123","mail":"nayana@gamil"}})