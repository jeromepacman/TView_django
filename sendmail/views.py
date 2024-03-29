from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm


def sendmail_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            checkbox = form.cleaned_data['checkbox']
            try:
                send_mail(subject, message, from_email, ['contact@tview.fr'])
            except BadHeaderError:
                messages.error(request, "Une erreur fatale est survenue")
            messages.success(request, "Votre message a été envoyé")
        else:
            messages.warning(request, "Formulaire non valide")
        return redirect('sendmail:sendmail')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
