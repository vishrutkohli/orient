import requests
import json
from django.http import HttpResponse
from main.models import data , Users 
from django.shortcuts import redirect



def index(request):
	uid = request.GET.get('uid')
	typeof = request.GET.get('typeof')
	date = request.GET.get('date')
	medicine = request.GET.get('medicine')
	duration = request.GET.get('duration')
	severity = request.GET.get('severity')

	v = Users.objects.get_or_create(uid = uid)[0]


	u = v.data_set.get_or_create()[0]
	#u.idm = v
	u.typeof = typeof 
	u.date = date
	u.medicine = medicine 
	u.duration = duration 
	u.severity = severity 
	u.save()

	return HttpResponse("saved")


def doc(request):

	uid = request.GET.get('uid')
	review = request.GET.get('review')
	v = Users.objects.get(uid = uid)


	u = v.data_set.get_or_create()[0]
	#u.idm = v
	u.review = review 
	u.save()
	return HttpResponse("saved")

def govt(request):
	uid = request.GET.get('uid')
	v = Users.objects.get(uid = uid)
	pk = v.pk
	u = data.objects.get(uid = pk)

	typeof = u.typeof
	date = u.date
	medicine = u.medicine
	duration = u.duration
	severity  = u.severity
	review = u.review

	response_obj = json.dumps({"typeof": typeof, "date":date , "medicine" :medicine , "duration" :duration, "severity" :severity, "review" :review})

	return HttpResponse(response_obj)	

	# u.review = q['review'] 


# Create your views here.
