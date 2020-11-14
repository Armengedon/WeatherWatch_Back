from django.urls import path

from . import views

urlpatterns = [
	#ex: /logger/
	path('', views.index, name='index'),
	#ex: /logger/3/
	path('<int:esp_id>/', views.detail, name='detail'),
	#ex: /logger/new/3/terrasa
	path('/new/<int:esp_id>/<str:esp_name>/', views.registerLogger, name='regLogger'),
	#ex: /logger/readings
	path('readings', views.readings, name='readings'),
]
