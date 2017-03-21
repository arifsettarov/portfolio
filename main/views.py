#!C:/Users/arif/AppData/Local/Programs/Python/Python35-32/python.exe
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf

from .models import projects,email
from .forms import SendEmailForm
import smtplib
from email.mime.text import MIMEText
def main_page(request):
    return render_to_response('main_page.html')

def portfolio(request):
    return render_to_response('portfolio.html')
def project(request):
    prjcts = projects.objects.all()
    args ={}
    args['projects'] = prjcts

    print(project)
    return render_to_response('projects.html', args)

def contacts(request):
    form = SendEmailForm
    args = {}
    args.update(csrf(request))
    args['form'] =form
    return  render_to_response('conpacts.html', args)

def sendemail(request):
    if request.POST:
        form = SendEmailForm(request.POST)
        if form.is_valid():
            form.save()
            leter = email.objects.get()

            message = MIMEText(leter.email+"\n"+leter.text,"","utf-8")
            message['Subject']= leter.name
            message['From']= "arif.settarov@mail.ru"
            message['To']= "arif.settarov@mail.ru"

            server = smtplib.SMTP('smtp.mail.ru',587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login("arif.settarov@mail.ru", "ctnnfhjdfhba")
            server.sendmail("arif.settarov@mail.ru", "arif.settarov@mail.ru", message.as_string())
            server.quit()
            leter.delete()
    return redirect('/contacts/')
