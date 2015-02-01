from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from urlparse import urlparse
import requests, json, datetime
import urllib


json_config = open('yelp_platform/config.json')
config = json.load(json_config)

def check_availability(request):
	response_data = {}
	response_data['availability_status'] = 'available'
	return HttpResponse(json.dumps(response_data), mime_type="application/json")

def generate_di_payload(active):
	payload = {
		"businesses":
		[
			{
				"matching_criteria":
					{"yelp_business_id": config.get('yelp_business_id')},
					"options":{"create_if_missing": "false","use_matching_criteria_for_update": "false"},
					"partner_business_id": "123",
					"update":
						{
							"platform_service":
							{
								"active": active,
								"ownership": "business",
								"types":
									[
										{
											"service_type": "booking_at_business",
											"hours":[{"day": "monday","start": "17:30:00","end": "22:00:00"}]
										}
									]
							}
						}
			}
		]
	}

	return payload

# Create your views here.
def activate(request):
	# build payload to activate a business
	# to-do get the yelp_business Id from config 
	# to-do read the business information from db
	payload = generate_di_payload("true")
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    # to-do remove the creds and store it in settings
	response = requests.post(
		config.get('data_ingestion_url'),
		auth=("yelp_dogfood", "mK6SxfPTEkSy9M46"),
		data=json.dumps(payload),
		headers=headers,
	)

	response_decoded = json.loads(response.text)

	try:
		job_id = response_decoded['job_id']
	except KeyError as e:
		return HttpResponse("Data Ingestion Error")

	return HttpResponse(job_id)

def deactivate(request):
	# build payload to de-activate a business
	payload = generate_di_payload("false")
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    # swap the code for an access token that grants the appropriate privilege needed
	response = requests.post(
		config.get('data_ingestion_url'),
		auth=("yelp_dogfood", "mK6SxfPTEkSy9M46"),
		data=json.dumps(payload),
		headers=headers,
	)

	response_decoded = json.loads(response.text)

	try:
		job_id = response_decoded['job_id']
	except KeyError as e:
		return HttpResponse("Data Ingestion Error")

	return HttpResponse(job_id)