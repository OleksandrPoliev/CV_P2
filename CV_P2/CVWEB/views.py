from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import ContactForm
from django.core.mail import send_mail


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

            return HttpResponseRedirect('/')
    else:
        form = ContactForm()
        return render(request, 'CVWEB/index.html', {'form': form})
