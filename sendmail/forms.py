from django import forms
from crispy_forms.helper import FormHelper


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nom",
        max_length=100
    )
    email = forms.EmailField(
        label="Email",
        max_length=100
    )
    subject = forms.ChoiceField(
        label="Sujet",
        choices=(
            ("No", "Choisissez..."), ("Perso", "Renseignements site perso"), ("Pro", "Renseignements site pro"),
            ("Tech", "Question technique"), ("Autre", "Autre"))
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea()
    )
    checkbox = forms.BooleanField(
        label="Vos informations restent confidentielles et conservées en format crypté"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()