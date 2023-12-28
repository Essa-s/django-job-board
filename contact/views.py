from django.shortcuts import render
from .models import Info
# Create your views here.
from django.core.mail import send_mail
from django.conf import settings
def send_message(request):
    info = Info.objects.first()
    
    if request.method == "POST":
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
    send_mail(
        subject,
        message +'   '+ email,
        email,
        [settings.EMAIL_HOST_USER],
        fail_silently=False,
        )
    return render(request, 'contact/contact.html',{'info':info})