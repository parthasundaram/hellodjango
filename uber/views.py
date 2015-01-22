from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from rauth import OAuth2Service
from urlparse import urlparse
import requests, json, datetime
from uber.models import User, Ride
from django.utils import timezone

json_config = open('uber/config.json')
config = json.load(json_config)

# Create your views here.

def generate_oauth_service():
	""" Prepare the OAuth2Service that is used to make requests later """
	return OAuth2Service(
		client_id = settings.UBER_CLIENT_ID,
		client_secret = settings.UBER_CLIENT_SECRET,
		name = config.get('name'),
	    authorize_url=config.get('authorize_url'),
	    access_token_url=config.get('access_token_url'),
	    base_url=config.get('base_uber_url')
	)

def generate_ride_headers(token):
	"""Generate the header object that is used to make API requests """
	return {
		'Authorization': 'bearer %s' % token,
		'Content-Type': 'application/json',
	}

def health(request):
	""" Check if the app is ok """
	return HttpResponse("All Ok")

def index(request):
	""" landing page """
	# make it look good, bootstrap fun!! 
	return render(request, 'uber/home.html')


def start_oauth(request):
	""" The first step in three-legged OAuth handshake """

	uber = generate_oauth_service()

	params = {
        'response_type': 'code',
        'redirect_uri': config.get('redirect_uri'),
        'scopes': ','.join(config.get('scopes'))
	}

	url = uber.get_authorize_url(**params)
	return HttpResponseRedirect(url)


def submit(request):
	""" Second step in OAuth. The user gets redirected back to our app, we need to get the code and swapit for a token """

	# retrieve the code from the URL (get param) that we received back from the server
	params = {
		'grant_type': 'authorization_code',
		'redirect_uri': config.get('redirect_uri'),
        'code': request.GET.get('code')
    }

    # swap the code for an access token that grants the appropriate privilege needed
	response = requests.post(
		config.get('access_token_url'),
		auth=(settings.UBER_CLIENT_ID, settings.UBER_CLIENT_SECRET),
		data=params,
	)

	request.session['access_token'] = response.json().get('access_token')

	# store this users data in the databasedd
	look_up_profile(request)

	# we have the access token - time to show some stuff
	return HttpResponseRedirect("history")
	
def history(request):
		# look up history but only look at last 50, looks like they paginate

	total_distance_travelled = 0
	longest_ride = 0
	shortest_ride = 0
	date_of_first_ride = timezone.now()


	user = User.objects.get(uber_uuid = request.session['user_uuid'])

	rides = user.ride_set.all()

	#params = {
	#	'offset':0,
	#	'limit':50,
	#}

	# issue the POST 
	#response_history = requests.get(
	#	config.get('base_uber_url_v1_1') + "history",
	#	headers= generate_ride_headers(request.session['access_token']),
	#	params = params,
	#)

	#response_decoded = json.loads(response_history.text)

	for ride in rides:
		total_distance_travelled += ride.distance
		if ride.distance > longest_ride:
			longest_ride = ride.distance

		if shortest_ride == 0:
			shortest_ride = ride.distance
		elif ride.distance < shortest_ride:
			shortest_ride = ride.distance

		if ride.start_time < date_of_first_ride:
			date_of_first_ride = ride.start_time


	total_distance_travelled = round (total_distance_travelled,2)

	return render(request, 'uber/history.html', {'ride_history': rides, 'total_distance_travelled': total_distance_travelled, 'longest_ride': longest_ride, 'shortest_ride': shortest_ride, 'date_of_first_ride':date_of_first_ride})


def look_up_profile(request):
	# look up the user and save the user info in the db

	response_me = requests.get(
		config.get('base_uber_url') + "me", 
		headers = generate_ride_headers(request.session['access_token']),
	)

	response_decoded = json.loads(response_me.text)

	user = User(first_name = response_decoded['first_name'], last_name = response_decoded['last_name'], 
		email = response_decoded['email'], uber_uuid = response_decoded['uuid'])

	user.save()

	request.session['user_uuid'] = response_decoded['uuid']

	# look up all the users rides and save it
	params = {
		'offset':0,
		'limit':50,
	}

	response_history = requests.get(
		config.get('base_uber_url_v1_1') + "history",
		headers= generate_ride_headers(request.session['access_token']),
		params = params,
	)

	response_decoded = json.loads(response_history.text)

	for ride in response_decoded['history']:
		r = Ride(user = user, 
			uuid =ride['uuid'],
			request_time = datetime.datetime.fromtimestamp(ride['request_time']),
			product_id = ride['product_id'],
			status = ride['status'],
			distance = ride['distance'],
			start_time = datetime.datetime.fromtimestamp(ride['start_time']),
			end_time = datetime.datetime.fromtimestamp(ride['end_time'])
		)
		r.save()

	return
