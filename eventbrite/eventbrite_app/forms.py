from django import forms
from betterforms.multiform import MultiModelForm

from .models import Volunteer,Participant

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['event','subevent', 'name', 'branch', 'semester', 'rollNumber', 'erp', 'work']
        
class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['event','subevent', 'name', 'branch', 'semester', 'rollNumber', 'erp', 'interest']

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']