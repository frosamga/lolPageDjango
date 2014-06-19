# Create your views here.
from django.shortcuts import render_to_response

def lol(request):
	return render_to_response(
		'templates/base.html',
		locals()
		)
