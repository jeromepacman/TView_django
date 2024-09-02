from django import forms
from django_recaptcha.fields import ReCaptchaField
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    email = forms.EmailField(
        label=_("Email"),
        max_length=50,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    subject = forms.ChoiceField(
        label=_("Subject"),
        choices=[
            ("select", _("...")),
            ("perso", _("About personal site")),
            ("pro", _("About pro site")),
            ("web3", _("About Web3 app")),
            ("bot", _("Telegram bot")),
            ("tech", _("Technical issue/offline service")),
            ("other", _("Other"))
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        label=_("Message"),
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    terms = forms.BooleanField(
        label=_("I agree to share my info on the contact form for Tview only"),
        required=True,
        widget=forms.CheckboxInput()
    )
    captcha = ReCaptchaField(
        label="",
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)









