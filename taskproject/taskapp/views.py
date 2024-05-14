from django.shortcuts import render
from django.http import HttpResponse
from . models import Place
from . models import Image
# Create your views here.
def demo(request):
     obj=Place.objects.all()
     obj1=Image.objects.all()
     return render(request,'index.html',{'result':obj,'result1':obj1})
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     res1=x*y
#     res2=x-y
#     res3=x/y
#     return render(request,'thank.html',{'result':res,'result1':res1,'result2':res2,'result3':res3})
