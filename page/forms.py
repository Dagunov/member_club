from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from .models import email_unique


class NewMemberForm(forms.Form):
	name = forms.CharField(label='Name', max_length=40,
		validators=[
			RegexValidator(
				'^[a-zA-Z .]*$',
				message='Name can only contain english letters, spaces and dots',
				code='invalid'),
		])
	email = forms.EmailField(label='Email')

	def clean_email(self):
		data = self.cleaned_data['email']
		if not email_unique(data):
			raise ValidationError(_('There already is a member with this email'), code='invalid')
		return data