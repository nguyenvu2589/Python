from django import forms
from pineapple.models import Page ,Category, Document
from pineapple.admin import UserProfile
from easy_thumbnails.fields import ThumbnailerImageField
from decimal import Decimal
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
	name  = forms.CharField(max_length=128, help_text="Enter the category name:")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = Category
		fields = ('name',)


class PageForm(forms.ModelForm):
	title = forms.CharField(max_length=128, help_text="Item name:")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	price = forms.DecimalField(max_digits=20, help_text="Price:")
	feature = forms.BooleanField(initial=False, help_text="Feature:")
	image = forms.ImageField(help_text="Upload image:")
	des = forms.CharField(max_length=999, help_text="Description:")
	slugP = forms.CharField(widget=forms.HiddenInput(), required=False)
	
	class Meta:
		model = Page
		exclude = ('category',)
		# or field =('title' , 'url' , 'views')
	
	def clean(self):
		cleaned_data = self.cleaned_data
		url = cleaned_data.get('url')

		if url and not url.startswith('http://'):
			url='http://' + url
			cleaned_data['url'] = url

		return cleaned_data

class DocumentForm(forms.ModelForm):
	name = forms.CharField(widget=forms.HiddenInput(),max_length=128, required = False)
	numEntry = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	
	class Meta:
		model = Document
		fields = {'document',}





class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('picture',)

