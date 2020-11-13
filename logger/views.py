from django.http import HttpResponse

from .models import Esp32, Reading

def index(request):
	return HttpResponse("Hello, world. You're at the logger index.")
	
def detail(request, esp_id):
	return HttpResponse("You are looking at esp32 %s." % esp_id)

def readings(request):
	response = ""
	for read in Reading.objects.all():
		response += str(read) + "\n"
	return HttpResponse(response)