from django import forms
from localflavor.us.forms import USStateSelect, USStateField
from crispy_forms.helper import FormHelper
from .models import *
from .widgets import *

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'
        widgets = {
            'birthDate' : DateSelect(),
            'state' : USStateSelect(),
        }
        labels = {
            'mc' : 'MC number',
            'usdot' : 'US DOT number',
            'gRate' : 'Rate',
        }

class BrokerForm(forms.ModelForm):
    class Meta:
        model = Broker
        fields = '__all__'
        widgets = {
            'state' : USStateSelect(),
        }
        labels = {
            'mc' : 'MC number',
            'usdot' : 'US DOT number',
        }

class OrderForm(forms.ModelForm):
    driver = forms.ModelChoiceField(queryset=Driver.objects.all(), empty_label="Choose")
    broker = forms.ModelChoiceField(queryset=Broker.objects.all(), empty_label="Choose")
    shipper = forms.ModelChoiceField(queryset=Shipper.objects.all(), empty_label="Choose", required=False)
    truck = forms.ModelChoiceField(queryset=Truck.objects.all(), empty_label="Choose", required=False)
    trailer = forms.ModelChoiceField(queryset=Trailer.objects.all(), empty_label="Choose", required=False)
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'origin_state' : USStateSelect(),
            'destination_state' : USStateSelect(),
            'pickup_date' : DateTimeSelect(),
            'delivery_date' : DateTimeSelect(),
            'payment_due' : DateSelect(),
        }
