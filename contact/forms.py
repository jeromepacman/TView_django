from django import forms


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
            (0, "Choisissez..."), (1, "Renseignements site perso"), (2, "Renseignements site pro"), (3, "Question technique"), (4, "Autre"))
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea,
        max_length=2000,
        required=True,
    )
    checkbox = forms.BooleanField(
        label="Mes informations seront temporairement conservées et resteront confidentielles"
    )