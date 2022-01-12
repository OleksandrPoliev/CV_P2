import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail ,BadHeaderError
from .models import FilesAdmin,Techskils
from .form import ContactForm,ContactFormz
from django.core.mail import EmailMessage

class CVPAGE (View):
    model = FilesAdmin
    def get(self,request,*args,**kwargs):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                subject = "Website cv "
                body = {
                    'Company': form.cleaned_data['Company'],
                    'Email': form.cleaned_data['Email'],
                    'Title': form.cleaned_data['Title'],
                    'Message': form.cleaned_data['Message'],
                }
                message = "\n".join(body.values())
                send_mail(subject, message, 'catering.warszawgo@gmail.com', ['oleksandrpoliev@gmail.com'])

                return HttpResponseRedirect('cv')
        else:
            form = ContactForm()
            return render(request, 'CVWEB/index.html', {'form': form})

def download (request):
    context={'file':FilesAdmin.objects.all(),"Techskils":Techskils.objects.all()}
    return render(request,'CVWEB/download.html',context)
def Down (request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as f:
            response=HttpResponse(f.read(),content_type='applicatoion/adminupload')
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    raise Http404







def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = "Website cv "
            body = {
                'Company': form.cleaned_data['Company'],
                'Email': form.cleaned_data['Email'],
                'Title': form.cleaned_data['Title'],
                'Message': form.cleaned_data['Message'],
            }
            message = "\n".join(body.values())
            send_mail(subject, message, 'catering.warszawgo@gmail.com', ['oleksandrpoliev@gmail.com'])




            return HttpResponseRedirect( 'cv')
    else:
        form = ContactForm()
        return render(request,'CVWEB/contact.html',{'form':form})

from django.shortcuts import render
from .form import ContactForm
from django.core.mail import send_mail


def cont (request):
    if request.method == "POST":
        subject = request.POST.get('subject',False)
        message = request.POST.get('message',False)
        sender = request.POST.get('sender',False)
        cc = request.POST.get('cc',False)
        send_mail("title", message, 'catering.warszawgo@gmail.com', ['daoka96@gmail.com'])
    return render(request, 'CVWEB/cont.html')