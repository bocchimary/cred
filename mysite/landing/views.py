from django.shortcuts import render


def landing(request):
       # return HttpResponse('Hello World')
    return render(request,'home.html')
  

def about(request):
      # return HttpResponse('My About Page')
     return render(request,'about.html')
  