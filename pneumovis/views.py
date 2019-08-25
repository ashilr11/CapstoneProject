#The view file handles certain requests from the browser.
#It links the html files to HttpRequests.
#Some of these requests are ‘GET’ or “POST” methods.
#These HttpRequests can be used to transfer and get data from the browser to the actual python scripts.

from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Incident
from .dataHandler import DataHandler
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64

from . import models

#The home(request) function gets data from the database, processes it using with matplotlab and creates a 3d histomgram as an overview graph.
def home(request):

	theIncidents = Incident.objects.all()
	obj = DataHandler()
	listOfData = obj.handleData(theIncidents)

	return render(request, 'pneumovis/home.html')

#The adddata(request) function reads the csv file, processes and uploads the file to the database.
def adddata(request):
	data = {}
	if "GET" == request.method:
		return render(request, "pneumovis/adddata.html", data)
	# if not GET, then proceed
	try:
		csv_file = request.FILES["csv_file"]
		if not csv_file.name.endswith('.csv'):
			messages.error(request,'File is not CSV type')
			print ("not csv")
			return HttpResponseRedirect(reverse("App-adddata"))

		file_data = csv_file.read().decode("utf-8")

		lines = file_data.split("\n")
		titles = lines[0].split(",")

		if (titles[0] != "participantID" or titles[1] != "npa_a4_growth" or
			titles[2] != "dateCollected" or titles[3] != "presence" or
			titles[4] != "dob" or titles[5] != "sex" or
			titles[6] != "hivExposed" or titles[7] != "site" or
			titles[8] != "serotype" or titles[9] != "vaccine" or titles[10] != "sequence"):
			messages.error(request,'CSV file is not in corrrect format, please check the format above and try again')
			return HttpResponseRedirect(reverse("App-adddata"))

		Incident.objects.all().delete()
		#loop over the lines and save them in db. If error , store as string and then display
		for i in range(len(lines)-1):
			fields = lines[i].split(",")
			participantID = fields[0]
			npa_a4_growth = fields[1]
			dateCollected = fields[2]
			presence = fields[3]
			dob = fields[4]
			sex = fields[5]
			hivExposed = fields[6]
			site = fields[7]
			serotype = fields[8]
			vaccine = fields[9]
			sequence = fields[10]
			newIncident = Incident(participantID=participantID, npa_a4_growth=npa_a4_growth, dateCollected=dateCollected, presence=presence, dob=dob,sex=sex,
										hivExposed=hivExposed, site=site, serotype=serotype, vaccine=vaccine, sequence=sequence)
			newIncident.save()
		messages.success(request, "Upload Successful")

	except Exception as e:
		messages.error(request,"Unable to upload file. "+repr(e))

	return HttpResponseRedirect(reverse("App-adddata"))

def datacards(request):
	return render(request, 'pneumovis/datacards.html')

def help(request):
	return render(request, 'pneumovis/help.html')

def about(request):
	return render(request, 'pneumovis/about.html')
