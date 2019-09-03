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
from .statistics import Statistics
from .plots import Plots
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt, mpld3
import numpy as np
from io import BytesIO
import base64
from . import models

# The home(request) function gets data from the database, processes it using matplotlab and creates some graphs and statistics
# The data the method returns contains html string for 3 graphs and six statistics all in the form of a dictionary

def home(request):
	plt.switch_backend('SVG')
	theIncidents = Incident.objects.all()
	obj = DataHandler()
	listOfData = obj.handleData(theIncidents)
	serotypeList = ["ST199","ST361","ST393","ST471","ST1447","ST2059","ST2062","ST2068","ST3358","ST3450","ST3983","ST4088","ST4893","ST5647","ST7052",
					"ST7345","ST8687","ST8838","ST10605","ST10673","ST10823","ST10854","ST13795","ST13797","ST13798","ST13799"]
	vaccinatedList = []
	notVaccinatedList = []
	maleList = []
	femaleList = []
	gugulethuList = []
	mandalayList = []
	hivExposedList = []
	presenceList = []
	# order of these indexes are from the list of data returned from the datahandler class
	for i in listOfData:
		vaccinatedList.append(i[4])
		notVaccinatedList.append(i[5]-i[4])
		maleList.append(i[0])
		femaleList.append(i[5]-i[0])
		gugulethuList.append(i[2])
		mandalayList.append(i[3])
		hivExposedList.append(i[1])
		presenceList.append(i[6])
	# create the plots
	plotObj = Plots()
	overviewGraph = plotObj.createOverview(hivExposedList, gugulethuList, mandalayList, maleList, femaleList, serotypeList)
	hivVsPresenceGraph = plotObj.createHivVsPresence(hivExposedList, presenceList)
	vaccinatedGraph = plotObj.createVaccineVsPresence(vaccinatedList, notVaccinatedList, presenceList)
	sitesGraph = plotObj.createSitesGraph(gugulethuList, mandalayList)
	#creates the stats
	statsObj = Statistics()
	data = {'overviewGraph': [overviewGraph],
			'hivVsPresenceGraph': [hivVsPresenceGraph],
			'vaccinatedGraph': [vaccinatedGraph],
			'sitesGraph': [sitesGraph],
			'noOfMales': statsObj.noOfMales(theIncidents),
			'noOfFemales': statsObj.noOfFemales(theIncidents),
			'noFromGugulethu': statsObj.noFromGugulethu(theIncidents),
			'noFromMandalay': statsObj.noFromMandalay(theIncidents),
			'noOfHivExposed': statsObj.noOfHivExposed(theIncidents),
			'noOfVaccinated': statsObj.noOfVaccinated(theIncidents)}

	return render(request, 'pneumovis/home.html', data )

# The adddata(request) function reads the csv file, processes and uploads the file to the database.
# It does not return any data in the response.
# The page is redirected to itself if there is an error when uploading the file. Error messages are shown
def adddata(request):
	data = {}
	if "GET" == request.method:
		return render(request, "pneumovis/adddata.html", data)
	# if not GET, then proceed
	try:
		csv_file = request.FILES["csv_file"]
		if not csv_file.name.endswith('.csv'):
			messages.error(request,'File is not CSV type')
			return HttpResponseRedirect(reverse("App-adddata"))

		file_data = csv_file.read().decode("utf-8")

		lines = file_data.split("\n")
		titles = lines[0].split(",")

		if (titles[0].lower() != "participantid" or titles[1].lower() != "npa_a4_growth" or
			titles[2].lower() != "datecollected" or titles[3].lower() != "presence" or
			titles[4].lower() != "dob" or titles[5].lower() != "sex" or
			titles[6].lower() != "hivexposed" or titles[7].lower() != "site" or
			titles[8].lower() != "serotype" or titles[9].lower() != "vaccine" or titles[10].lower() != "sequence"):
			messages.error(request,'CSV file is not in corrrect format, please check the format above and try again')
			return HttpResponseRedirect(reverse("App-adddata"))

		Incident.objects.all().delete()
		#loop over the lines and save them in db.
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

# method gets all incidents and uses the datahandler class to get the list of data which it returns in the htmlresponse
# this data can be then used in the html code of the datacards page

def datacards(request):
	theIncidents = Incident.objects.all()
	obj = DataHandler()
	listOfData = obj.handleData(theIncidents)
	data = {'array': listOfData}

	return render(request, 'pneumovis/datacards.html', data)

# method simply returns a HttpResponse to the help page
def help(request):
	return render(request, 'pneumovis/help.html')

# method simply returns a HttpResponse to the about page
def about(request):
	return render(request, 'pneumovis/about.html')
