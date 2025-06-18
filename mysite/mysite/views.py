from django.shortcuts import render


def landing(request):
       # return HttpResponse('Hello World')
    return render(request,'home.html')
  

def trial(request):
      # return HttpResponse('My About Page')
     return render(request,'trial.html')
  