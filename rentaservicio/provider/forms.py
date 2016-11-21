from django.forms import ModelForm, HiddenInput
from client.models import ClientProvider

class ClientProviderForm(ModelForm):
    class Meta:
        model = ClientProvider
        fields = ('providerplace',)
        widgets = {
            'providerplace': HiddenInput(),
        }