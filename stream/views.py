from django.http import HttpResponse

def home(request):
	return HttpResponse('I am responding to a request.')