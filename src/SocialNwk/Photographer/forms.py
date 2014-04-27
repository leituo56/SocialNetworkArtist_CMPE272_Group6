__author__ = 'leituo56'

from django import forms


class DocumentForm(forms.Form):
    title = forms.CharField(min_length=2, max_length=30, label='Title', help_text='max. 30 characters')
    file = forms.FileField(label='Select a file', help_text='max. 42 megabytes')