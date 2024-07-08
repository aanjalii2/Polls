from django import forms
from .models import Poll, Choice, Vote

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['choice']
