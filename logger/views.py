from django.http import HttpResponse

from .models import Esp32, Reading

def index(request):
	return HttpResponse("Hello, world. You're at the logger index.")
	
def registerLogger(request, id, name):

	if not Esp32.objects.filter(esp_id=id).exists():
		logger = Esp32(esp_id=id, esp_name=name)
		logger.save()
	response = ""
	for logg in Esp32.objects.all():
		response += str(logg) + "\n"
	return HttpResponse(response)

	
def detail(request, esp_id):
	return HttpResponse("You are looking at esp32 %s." % esp_id)

def readings(request):
	response = ""
	for read in Reading.objects.all():
		response += str(read) + "\n"
	return HttpResponse(response)