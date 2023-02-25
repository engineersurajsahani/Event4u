from django import forms

from .models import Volunteer,Participant,Audience,Payment

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['event','subevent', 'name', 'branch', 'semester', 'rollNumber', 'erp', 'work']
        
class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['event','subevent', 'name', 'branch', 'semester', 'rollNumber', 'erp', 'interest']

class AudienceForm(forms.ModelForm):
    class Meta:
        model = Audience
        fields = ['event', 'name', 'branch', 'semester', 'rollNumber', 'erp']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['event', 'paymentRecieptImage', 'recieptNumber', 'name', 'branch', 'semester', 'rollNumber', 'erp', 'whatsAppNumber', 'mobileNumber']
        widgets = {
            'paymentRecieptImage': forms.ClearableFileInput(attrs={'required': False}),
        }

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].required = False

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']