from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.template.loader import render_to_string
from .forms import ContactForm


def sendmailView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            checkbox = form.cleaned_data['checkbox']
            try:
                send_mail(subject, message, from_email, ['contact@tview.fr'])
            except BadHeaderError:
                messages.error(request, "Une erreur fatale est survenue")
            # template = render_to_string('confirmation.html', {'name': name})
            # email_conf = EmailMessage('TView confirmation de réception', template, 'contact@tview.fr', [from_email])
            # email_conf.fail_silently = False
            # email_conf.send()
            messages.success(request, "Votre message a été envoyé, merci")
        else:
            messages.warning(request, "Formulaire non valide")
        return redirect('/sendmail')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})