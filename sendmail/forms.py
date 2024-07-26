from django import forms
from django_recaptcha.fields import ReCaptchaField
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper


class ContactForm(forms.Form):
    email = forms.EmailField(
        label=_("Email"),
        max_length=50
    )
    subject = forms.ChoiceField(
        label=_("Subject"),
        choices=(
            ("No", _("...")),
            ("Perso", _("About personal site")),
            ("Pro", _("About pro site")),
            ("Tech", _("Technical issue")),
            ("Other", _("Other"))
        )
    )
    message = forms.CharField(
        label=_("Message"),
        widget=forms.Textarea(attrs={'rows': '6', 'cols': '40'})
    )
    checkbox = forms.BooleanField(
        label=_("I agree to share my information on the contact form for Tview only"),
        widget=forms.CheckboxInput()
    )
    captcha = ReCaptchaField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
