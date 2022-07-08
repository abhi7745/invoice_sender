from django.shortcuts import render

# Create your views here.

# email sending
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

from django.contrib import messages

def index(request):

    html_template = 'email_template.html'
    html_message = render_to_string(html_template)
    subject = 'Trail from pythonanywhere'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['']
    message = EmailMessage(subject, html_message,
                            email_from, recipient_list)
    message.content_subtype = 'html'
    message.send()
    print('email sended')
    messages.success(request, 'Message sended successfully')

    return render(request,'index.html')