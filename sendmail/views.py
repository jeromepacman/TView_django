from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm

from django.utils.translation import gettext_lazy as _


def sendmail_view(request):
    """Handle sending of emails via contact form."""

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            terms = form.cleaned_data['terms']
            try:
                send_mail(subject, message, from_email, ['contact@tview.fr'])
                messages.success(request, _("Your message has been sent. Thank you for your interest"))
            except BadHeaderError:
                messages.error(request, _("Invalid header found !"))
        else:
            messages.warning(request, _("You haven't resolved the captcha. Please try again"))
        return redirect('sendmail:sendmail')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

