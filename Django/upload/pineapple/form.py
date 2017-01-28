from django import forms
from pineapple.models import Document
from easy_thumbnails.fields import ThumbnailerImageField
from decimal import Decimal
from django.contrib.auth.models import User


class DocumentForm(forms.ModelForm):
	name = forms.CharField(widget=forms.HiddenInput(),max_length=128, required = False)
	numEntry = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	
	class Meta:
		model = Document
		fields = {'document',}

