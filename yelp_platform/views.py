from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from urlparse import urlparse
import requests, json, datetime

json_config = open('yelp_platform/config.json')
config = json.load(json_config)

# Create your views here.
def index(request):
	""" landing page """
	# make it look good, bootstrap fun!! 
	params = {
		"matching_criteria":{
			"yelp_business_id": config.get('yelp_business_id'),
		},
		"options":{
			"create_if_missing": false,
			"use_matching_criteria_for_update": false,
		},
		"partner_business_id": "123",
		"update":{
			"platform_service":{
				"active": true,
				"ownership": "business",
				"service_types":[
					{
						"service_type": "booking_at_business",
						"hours”: [
								{
									“day”: “monday”,
									“start”: “17:30:00”,
									“end”: “22:00:00”
								}
							],
							"exceptions”: [
								{
									“date”: “2013-07-04”,
									“start”: “18:00:00”,
									“end”: “21:00:00”
								}
							]
					}
				]
			}
		}
    }

    # swap the code for an access token that grants the appropriate privilege needed
	response = requests.post(
		config.get('data_ingestion_url'),
		auth=("yelp_dogfood", "mK6SxfPTEkSy9M46"),
		data=params,
	)
	return HttpResponse(response.json().get('job_id'))