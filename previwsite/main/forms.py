from .models import Registration
from django.forms import ModelForm, TextInput


class RegForm(ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'mail', 'twsub', 'twretweet', 'telsubchannel', 'telsubgroup']
        widgets = {"name": TextInput(attrs={
            'class': 'input',
            "placeholder": "Full name",
            'required pattern': "[a-zA-Z]+",
            'title': "The name can only contain letters."
            }),
            "mail": TextInput(attrs={
                'class': 'input',
                "placeholder": "Mail",
                'type': "email",
            }),
            "twsub": TextInput(attrs={
                'class': 'input',
                "placeholder": "Twitter username",
                'required minlength': '1',
                'required maxlength': "128",
                'type': 'text'
            }),
            "twretweet": TextInput(attrs={
                'class': 'input',
                "placeholder": "Retweet link",
                'required minlength': '1',
                'required maxlength': "128",
                'type': 'text'
            }),
            "telsubchannel": TextInput(attrs={
                'class': 'input',
                "placeholder": "Telegram link start with @",
                'required minlength': '1',
                'required maxlength': "128",
                'type': 'text'
            }),
            "telsubgroup": TextInput(attrs={
                'class': 'input',
                "placeholder": "Telegram link start with @",
                'required minlength': '1',
                'required maxlength': "128",
                'type': 'text'
            })
        }