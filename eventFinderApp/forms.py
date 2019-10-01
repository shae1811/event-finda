from django.forms import ModelForm, SplitDateTimeField
from django.contrib.admin import widgets
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Event, Category, Account

class EventForm(ModelForm):
    start_time = SplitDateTimeField(widget=widgets.AdminSplitDateTime())
    end_time = SplitDateTimeField(widget=widgets.AdminSplitDateTime())

    class Meta:
        model = Event
        fields = ['host', 'title','location','venue','start_time','end_time','category']
        widgets = {'start_time': widgets.AdminSplitDateTime, 'end_time': widgets.AdminSplitDateTime,}
        exclude = ['host']

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = [
            'first_name',
            'surname',
            'email'
        ]