from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.shortcuts import render
from django.template.loader import render_to_string
from .forms import ContactForm


def contactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['contact@tview.fr'])
            except BadHeaderError:
                messages.error(request, 'une erreur exceptionnelle est survenue')
            template = render_to_string('confirmation.html', {'name': name})
            email_conf = EmailMessage('Votre message à bien été reçu', template, settings.EMAIL_HOST_USER, [from_email])
            email_conf.fail_silently = False
            email_conf.send()
            messages.success(request, "  Votre message à été envoyé! Vous allez recevoir un message de confirmation")
        else:
            messages.warning(request, "Veuillez bien remplir tous les champs, merci")
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})