# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from pineapple.models import Category, Document
from pineapple.models import Page
from pineapple.form import CategoryForm
from pineapple.form import PageForm, DocumentForm 
from pineapple.form import UserForm, UserProfileForm
from django.shortcuts import render
from easy_thumbnails.files import get_thumbnailer
from django.core.files.storage import FileSystemStorage
from datetime import datetime
import csv

def index(request):
	category_list = Category.objects.all()
	page_list = Page.objects.all()[:5]
	feature   = Page.objects.filter(feature=True)
	top_five  = Page.objects.order_by('-views')[:4]
	context_dict = { 'categories': category_list , 'pages': page_list, 'top5':top_five, 'ft': feature}

	# request for number of last visit 
	# from server if not valid , set it to 1

	response = render(request, 'pineapple/index.html', context_dict)


	return response


def about(request):
	return render_to_response('pineapple/about.html')


def menu(request):
	context_dict = {}
	try:
		cat = Category.objects.all()

		#context_dict['category_name'] = category
		context_dict['category'] = cat
		pages = Page.objects.all()
		
		context_dict['page'] = pages
	except Category.DoesNotExist:
		print " does not exist"

	return render(request, 'pineapple/menu.html', context_dict)

def display(request):
	context_dict = {}
	try:
		cat = Category.objects.all()

		#context_dict['category_name'] = category
		context_dict['category'] = cat
		pages = Page.objects.all()
		
	

		context_dict['page'] = pages
	except Category.DoesNotExist:
		print " does not exist"

	return render(request, 'pineapple/display.html', context_dict)

def order(request):
	context_dict = {}
	try:
		cat = Category.objects.all()
		i = 0
		#context_dict['category_name'] = category
		context_dict['category'] = cat
		context_dict['count'] = i
		pages = Page.objects.all()
		
		context_dict['page'] = pages
	except Category.DoesNotExist:
		print " does not exist"

	return render(request, 'pineapple/order.html', context_dict)

def contact (request):
	context_dict={}

	return render(request, 'pineapple/contact.html', context_dict)


def category(request, category_name_slug):
	context_dict = {}
	try:

		category = Category.objects.get(name=category_name_slug)
		
		context_dict['category_name'] = category.name

		pages = Page.objects.filter(category=category)
		context_dict['page'] = pages
		context_dict['category'] = category
		context_dict['category_name_slug'] = category_name_slug 
	except Category.DoesNotExist:
		print " does not exist"
	return render(request, 'pineapple/category.html', context_dict)

def page(request, page_name_slug):

	context_dict ={}
	try:
		print (page_name_slug)
		page =Page.objects.get(slugP = page_name_slug)
		context_dict['item'] = page

	except Page.DoesNotExist:
		print "cant find this page."

	return render(request, 'pineapple/page.html', context_dict)

def add_category(request):
	if request.method =='POST':
		form = CategoryForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print form.errors
	else: 
		form = CategoryForm()

	return render(request, 'pineapple/add_category.html', {'form' : form})
	

def add_page(request, category_name_slug):
	try : 
		cat = Category.objects.get(slug=category_name_slug)
	except Category.DoesNotExist:
		cat = None

	if request.method == 'POST':
		form =PageForm(request.POST)
		if form.is_valid():
			page = form.save(commit=False)
			page.category = cat
			page.views = 0
			page.save()
			return category(request, category_name_slug)
		else: 
			print form.errors
	else:
		form = PageForm()
	context_dict = {'form': form, 'category': cat }
	return render(request, 'pineapple/add_page.html', context_dict)

def upload(request):
	try:
		docs = Document.objects.order_by('-time')[:5]
	except Document.DoesNotExist:
		docs = None
	context_dict ={}
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			name = request.FILES['document']
			doc = form.save(commit = False)
			doc.time = datetime.now()
			doc.name = name
			print doc.name, "this is doc name"
			doc.numEntry = parse_csv(name)
			doc.save()
			context_dict['docs'] = docs
		else :
			print form.errors
	else:
		form = DocumentForm()

	context_dict = {'form': form, 'docs': docs }
	return render(request, 'pineapple/upload.html', context_dict )

# description .... 1. take it out / 2. change to name,
# after click choose file -> name change to file name

# create history table and delete history. ...

def parse_csv(upload):
	count = 0
	reader = csv.reader(upload)
	for line in reader:
		# do something with line...
		count += 1
	return count



