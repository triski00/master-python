from django import forms
from django.core import validators

class FormArticle(forms.Form):
    title = forms.CharField(
        label="Título",
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Mete el título',
                'class': 'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'El título es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9-]*$', message='El título está mal formado')
        ]
    )

    content = forms.CharField(
        label="Contenido",
        widget=forms.Textarea
    )

    public_options = [
        ('1', 'Sí'),
        ('0', 'No')
    ]

    public = forms.TypedChoiceField(
        label="¿Publicado?",
        choices=public_options
    )

