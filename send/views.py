from django.shortcuts import render
from django.core.mail import send_mail
def index(request):
    send_mail('hall world here is Ahmed  ','helloja wheor adlfj a','hwlerjjadfre',['ahmedbaset092@gmail.com'],fail_silently=False)
    return render(request,'send/index.html')
# Create your views here.
