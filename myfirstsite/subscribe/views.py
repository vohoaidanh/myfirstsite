from django.shortcuts import render, HttpResponse
from myfirstsite.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail

# Create your views here.
#DataFlair #Send Email
def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to DataFlair'
        message = 'Hope you are enjoying your Django Tutorials'
        recepient = str(sub['Email'].value())
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'subscribe/success.html', {'recepient': recepient})

    return render(request, 'subscribe/index.html', {'form':sub})

def hello(request):
    return render(request,'subscribe/hello.html')


#DataFlair #Form #View Functions
def regform(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        html = 'we have recieved this form again'
    else:
        html = 'welcome for first time'
    return render(request, 'subscribe/signup.html', {'html': html, 'form': form})