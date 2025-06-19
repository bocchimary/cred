from django.shortcuts import render

#LANDING PAGE
def landing(request):
    return render(request,'home.html')
#OTP PAGE
def otp(request):
     return render(request,'otp.html')
  
#trial page
def trial(request):
     return render(request,'trial.html')

def students(request):
     return render(request,'students.html')