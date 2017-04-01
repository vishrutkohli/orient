
import requests
import json
from django.http import HttpResponse
from api.models import data , Users , login , Saved 
from django.shortcuts import redirect


acess_token = 'AQWaKPLlQEPw-T3-sUakDt6XMpLMU1iuDpz9jzKKySirZxoOEmSwnR_CHPePahHU3eSJ7m5qx2V55jYGe99F5fUs4gjR-1P__bzn0v6Y04YC9ZVMtwMbhCzc7GzZ2Gywmy5NNKGXXsfV_BhGiiTncLTFOXJQrCvEZfiiRATfepeHZbfUWX0'
# Create your views here.

def index(request):
	# payload1 = {'response_type': 'code', 'state': '123456789', 'redirect_uri': 'https://fathomless-depths-13330.herokuapp.com/', 'client_id': '86xgcoikz5tvem' }
	# p = requests.get('https://www.linkedin.com/oauth/v2/authorization', params=payload1)
	# print(p)
	


	




	code = request.GET.get('code')
	print code 

	




	payload = {'grant_type': 'authorization_code', 'code': code , 'redirect_uri': 'http://178.62.41.110:88/linkedin/', 'client_id': '86xgcoikz5tvem', 'client_secret': 'bMGSpxX8XNEpxocO'}

	r = requests.post('https://www.linkedin.com/oauth/v2/accessToken', params=payload)
	t = json.loads(r.text)
	z = t['access_token']
	print "hihihihi" + z
	x = requests.get('https://api.linkedin.com/v1/people/~:(id,first-name,email-address,last-name,headline,picture-url,public-profile-url,location,summary,specialties,positions)?format=json', 
                    headers={"Authorization": "Bearer " + z
                     },
                  )
	q = json.loads(x.text)
	idn = q['id']
	v = Users.objects.get_or_create(idn = idn)[0]
	v.idn = idn
	pk = v.pk
	v.save()

	u = v.data_set.get_or_create()[0]
	#u.idm = v
	u.first_name = q['firstName'] 
	u.last_name = q['lastName'] 
	u.headline = q['headline'] 
	u.location = q['location'] 
	try:

		u.summary = q['summary'] 

	except:
		u.summary = "NULL"
	
	try:

		u.specialties = q['specialties'] 

	except:
		u.specialties = "NULL"
				
	

	try:


		u.picture_url = q['pictureUrl'] 

	except:
		u.picture_url = "NULL"
		

	u.public_profile_url = q['publicProfileUrl'] 
	u.email_address = q['emailAddress'] 
	u.positions = q['positions']
	u.save()





	responseobj = json.dumps(q, indent = 4)






	return HttpResponse(responseobj,content_type = "application/json")


def return_data(request):
	mac_address = request.GET.get('mac_address')


	u = data.objects.get(mac_address = mac_address)

	first_name = u.first_name
	last_name = u.last_name
	headline = u.headline
	summary = u.summary
	location  = u.location
	specialties = u.specialties
	picture_url = u.picture_url
	public_profile_url = u.public_profile_url
	email_address = u.email_address
	positions = u.position


	response_obj = json.dumps({"first_name": first_name, "last_name":last_name , "headline" :headline , "summary" :summary, "location" :location, "specialties" :specialties, "picture_url" :picture_url, "public_profile_url" :public_profile_url, "email_address" :email_address, "positions" :positions })

	return HttpResponse(response_obj)	


def autocall(request):
	idn = request.GET.get('id')

	mac_address = request.GET.get('mac_address')



	# mac_address = request.GET.get('mac_address')
	v = Users.objects.get(idn = idn)
	pk = v.pk

	u = data.objects.get(idm = pk)

	u.mac_address = mac_address
	
	u.save()

	return HttpResponse("saved")



def login_orient(request):
	mac_address = request.GET.get('mac_address')
	email = request.GET.get('email')
	password = request.GET.get('password')




	v = login.objects.get_or_create(email = email)[0]
	v.password1 = password


	v.save()
	number = v.pk


	newid = str(number) + "orient"
	m = Users.objects.create(idn = newid)
	m.save()


	u = m.data_set.create(email_address = email)
	u.mac_address = mac_address
	u.save()

	return HttpResponse("created")


def update_data(request):

	# idn = request.GET.get('id')
	first_name = request.GET.get('first_name')
	mac_address = request.GET.get('mac_address')
	last_name = request.GET.get('last_name')
	headline = request.GET.get('headline')
	summary = request.GET.get('summary')
	location = request.GET.get('location')
	specialties = request.GET.get('specialties')
	picture_url = request.GET.get('picture_url')
	public_profile_url = request.GET.get('public_profile_url')
	# email_address = request.GET.get('email_address')
	position = request.GET.get('positions')


	# mac_address = request.GET.get('mac_address')
	u = data.objects.get(mac_address = mac_address)


	# u = data.objects.get_or_create(idn = idn)[0]
	# u.mac_address = mac_address
	u.first_name = first_name
	u.last_name = last_name
	u.headline = headline
	u.summary = summary
	u.location  = location
	u.specialties = specialties
	u.picture_url = picture_url
	u.public_profile_url = public_profile_url
	# u.email_address = email_address
	u.position = position
	u.save()

	return HttpResponse("saved")	


# def saved(request):
# 	idn = request.GET.get('id')
# 	sidn = request.GET.get('sid')

# 	v = Users.objects.get(idn = idn)
# 	pk = v.pk
# 	u = v.saved_set.create()
# 	u.saved_id = sidn
# 	u.save()

# 	return redirect( '/return_data?mac_adre=' + sidn )






	
