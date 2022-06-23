from tview import prod_settings
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
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            checkbox = form.cleaned_data['checkbox']
            try:
                send_mail(
                subject,
                message,
                    email ,
                ["contact@tview.fr"],
                )
            except BadHeaderError:
                 messages.error(request, 'une erreur exceptionnelle est survenue')
            template = render_to_string('confirmation.html', {'name': name})
            email_conf = EmailMessage('Votre message a bien été reçu', template, prod_settings.EMAIL_HOST_USER, [email])
            email_conf.fail_silently = False
            email_conf.send()

            messages.success(request, "  Votre message a été envoyé, merci")
        else:
            messages.error(request, 'Veuillez remplir correctement tous les champs. Merci')

    form = ContactForm()
    return render(request, 'contact.html', {'form': form})