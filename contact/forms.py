from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Nom', max_length=100)
    from_email = forms.EmailField(label='Email')
    subject = forms.ChoiceField()
    message = forms.CharField(widget=forms.Textarea)