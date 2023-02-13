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