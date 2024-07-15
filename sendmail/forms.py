from crispy_forms import helper
from django import forms
from django_recaptcha.fields import ReCaptchaField
from crispy_forms.helper import FormHelper
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):

    email = forms.EmailField(
        label="Email",
        max_length=50
    )
    subject = forms.ChoiceField(
        label="Sujet",
        choices=(
            ("No", "..."), ("Perso", "Renseignements site perso"), ("Pro", "Renseignements site pro"),
            ("Tech", "Question technique"), ("Autre", "Autre"))
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea()
    )
    checkbox = forms.BooleanField(
        label="Vos informations restent confidentielles et conservées en format crypté, no spam"
    )
    captcha = ReCaptchaField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        helper.form_class = 'form-horizontal'
        helper.label_class = ''
