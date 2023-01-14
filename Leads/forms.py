from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField

from .models import Lead, User


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'cell_num',
            'e_mail',
            'addons',
            'agent',
        )


class LeadForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    cell_num = forms.IntegerField()
    e_mail = forms.CharField(max_length=50)
    addons = forms.FileField(required=False)


class NewUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
