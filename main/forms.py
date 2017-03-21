# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import email
class SendEmailForm(ModelForm):
    class Meta:
        model = email
        fields =['name','email','text']

    def __init__(self, *args, **kwargs):
        super(SendEmailForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':"uk-input uk-margin-small",'placeholder':"ФИО"})
        self.fields['email'].widget.attrs.update({'class':"uk-input uk-margin-small",'placeholder':"E-mail"})
        self.fields['text'].widget.attrs.update({'class':"uk-textarea uk-margin-small", 'rows':"5",'placeholder':"Сообщение"})