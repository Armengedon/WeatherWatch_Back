import datetime

from django.db import models
from django.utils import timezone

class Esp32(models.Model):
	esp_id = models.IntegerField(default = 0)
	esp_name = models.CharField(max_length=20)
	
	def __str__(self):
		return self.esp_name;
	
class Reading(models.Model):
	reading_source = models.ForeignKey(Esp32, on_delete=models.CASCADE)
	reading_temp = models.IntegerField(default = 0)
	reading_hum = models.IntegerField(default = 0)
	reading_date = models.DateTimeField('Reading date')
	
	def was_published_recently(self):
		return self.reading_date >= timezone.now() - datetime.timedelta(days=1)
	
	def __str__(self):
		aux = ""
		aux += str(self.reading_temp) + "ºC "
		aux += str(self.reading_hum) + "% "
		aux += str(self.reading_date)
		return aux;