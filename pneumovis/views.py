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
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt, mpld3
import numpy as np
from io import BytesIO
import base64

from . import models

#The home(request) function gets data from the database, processes it using with matplotlab and creates a 3d histomgram as an overview graph.
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

	for i in listOfData:
		vaccinatedList.append(i[4])
		notVaccinatedList.append(i[5]-i[4])
		maleList.append(i[0])
		femaleList.append(i[5]-i[0])
		gugulethuList.append(i[2])
		mandalayList.append(i[3])
		hivExposedList.append(i[1])
	groups = 26
	# create plot
	fig, ax = plt.subplots(figsize=(18,7.5))
	index = np.arange(groups)
	bar_width = 0.35
	opacity = 0.75

	stems1 = plt.stem(index, hivExposedList, label='Hiv Exposed', linefmt='C9-', markerfmt='C9x')
	rects1 = plt.bar(index, gugulethuList, bar_width,
	alpha=opacity,
	color='b',
	label='Guguletho')

	rects2 = plt.bar(index + bar_width, mandalayList, bar_width,
	alpha=opacity,
	color='k',
	label='Mandalay', hatch='/')

	lines1 = plt.plot(index, maleList, marker='o', color='r', label='Males')
	lines2 = plt.plot(index, femaleList, marker='o', color='y', label='Females')

	plt.xlabel('Serotypes')
	plt.ylabel('Number of Incidents')
	plt.xticks(index + bar_width, serotypeList)
	plt.legend()
	plt.tight_layout()
	html_graph = mpld3.fig_to_html(fig)
	statsObj = Statistics()
	data = {'graph': [html_graph],
	 		'noOfMales': statsObj.noOfMales(theIncidents),
			'noOfFemales': statsObj.noOfFemales(theIncidents),
			'noFromGugulethu': statsObj.noFromGugulethu(theIncidents),
			'noFromMandalay': statsObj.noFromMandalay(theIncidents),
			'noOfHivExposed': statsObj.noOfHivExposed(theIncidents),
			'noOfVaccinated': statsObj.noOfVaccinated(theIncidents)}

	return render(request, 'pneumovis/home.html', data )

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
