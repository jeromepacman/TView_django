from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.shortcuts import render
from django.template.loader import render_to_string


def contactView(request):
    name = request.POST.get('nom')
    from_email = request.POST.get('email')
    subject = request.POST.get('sujet')
    message = request.POST.get('message')

    if message and from_email and subject != "0" and name:
        try:
            send_mail(subject, message, from_email, ['contact@tview.fr'])
        except BadHeaderError:
            messages.error(request, 'une erreur exceptionnelle est survenue')
        template = render_to_string('confirmation.html', {'name': name})
        email_conf = EmailMessage('Votre message à bien été reçu', template, settings.EMAIL_HOST_USER, [from_email])
        email_conf.fail_silently = False
        email_conf.send()
        messages.success(request, "Votre message à été envoyé! Vous allez recevoir un message de confirmation")

    elif message or from_email or name:
        messages.warning(request, "Veuillez remplir tous les champs, merci")

    return render(request, 'contact.html', )