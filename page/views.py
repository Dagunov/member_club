from django.shortcuts import render

from .models import Member, add_member, members
from .forms import NewMemberForm

import logging


def index(request):
	logger = logging.getLogger(__name__)
	logger.info(pretty_request(request))

	global members
	print(members)
	if request.method == 'POST':
		form = NewMemberForm(request.POST)
		if form.is_valid():
			add_member(Member(form.cleaned_data['name'], form.cleaned_data['email']))
			form = NewMemberForm()
	else:
		form = NewMemberForm()
	
	context = {
		'members': members,
		'form': form,
	}
	response = render(request, 'index.html', context)
	logger.info(pretty_response(response))
	return response


def pretty_request(request):
	try:
		headers = ''
		for header, value in request.META.items():
			if not header.startswith('HTTP'):
				continue
			header = '-'.join([h.capitalize() for h in header[5:].lower().split('_')])
			headers += '{}: {}\n'.format(header, value)

		return (
			'{method} HTTP/1.1\n'
			'Content-Length: {content_length}\n'
			'Content-Type: {content_type}\n'
			'{headers}\n'
			'{body}'
		).format(
			method=request.method,
			content_length=request.META['CONTENT_LENGTH'],
			content_type=request.META['CONTENT_TYPE'],
			headers=headers,
			body=request.body,
		)
	except Exception as e:
		return 'Wrongly formatted HTTP request, ' + str(e)

def pretty_response(response):
	return (
		'HTTPResponse {status_code} {reason_phrase}\n'
		'Headers: {headers}\n'
		'Content: {content}'
	).format(
		status_code=response.status_code,
		reason_phrase=response.reason_phrase,
		headers=response.headers,
		content=response.content
	)