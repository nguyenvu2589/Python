# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from pineapple.models import Document
from pineapple.form import DocumentForm 
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from datetime import datetime
import csv


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


def parse_csv(upload):
	count = 0
	reader = csv.reader(upload)
	for line in reader:
		# do something with line...
		count += 1
	return count



