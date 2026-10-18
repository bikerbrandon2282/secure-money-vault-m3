from .models import transaction
from django import forms
from django.forms import DateTimeInput, Select
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Layout, MultiField, Row, Column


class TransactionForm(forms.ModelForm):
    class Meta:
        model = transaction
        fields = ['description', 'amount', 'type', 'date', 'currency', 'category']
        widgets = {
            'date': DateTimeInput(format='%Y-%m-%dT%H:%M',attrs={'type': 'datetime-local', 'class': 'width-small'}),
            'currency' : Select(attrs={'class': 'width-small'}),
            'category': Select(attrs={'class': 'width-small'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'description',
            'amount',
            'type',
            'date',
            'currency',
            'category',
        )
        print("FORM FIELDS:", list(self.fields.keys()))