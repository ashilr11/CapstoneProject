from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Incident
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

from . import models

def home(request):
	theIncidents = Incident.objects.all()
	yaxisNames = ('35B(361)', '21(10854)', '15B/C(8687)', '19A(2062)', '16F(3450)')
	xaxisNames = ('male', 'hivExposed', 'guguletho', 'mandalay', 'total')
	list = []
	maleCount, hivExposedCount, gugulethoCount, mandalayCount, totalCount = 0
	for i in theIncidents:
		if (i.sequence == '361' and i.sex == 'Male'):
			maleCount += 1
		if (i.sequence == '361' and i.hivExposed == 'Yes'):
			hivExposedCount += 1
		if (i.sequence == '361' and i.site == 'Guguletho'):
			gugulethoCount += 1
		if (i.sequence == '361' and i.site == 'Mandalay'):
			mandalayCount += 1
		if (i.sequence == '361'.translate(None, "*~")):
			total += 1
	list.append([maleCount, hivExposedCount, gugulethoCount, mandalayCount, totalCount])

	for i in theIncidents:
		if (i.sequence == '10854' and i.sex == 'Male'):
			maleCount += 1
		if (i.sequence == '10854' and i.hivExposed == 'Yes'):
			hivExposedCount += 1
		if (i.sequence == '10854' and i.site == 'Guguletho'):
			gugulethoCount += 1
		if (i.sequence == '10854' and i.site == 'Mandalay'):
			mandalayCount += 1
		if (i.sequence == '10854'.translate(None, "*~")):
			total += 1
	list.append([maleCount, hivExposedCount, gugulethoCount, mandalayCount, totalCount])

	for i in theIncidents:
		if (i.sequence == '8687' and i.sex == 'Male'):
			maleCount += 1
		if (i.sequence == '8687' and i.hivExposed == 'Yes'):
			hivExposedCount += 1
		if (i.sequence == '8687' and i.site == 'Guguletho'):
			gugulethoCount += 1
		if (i.sequence == '8687' and i.site == 'Mandalay'):
			mandalayCount += 1
		if (i.sequence == '8687'.translate(None, "*~")):
			total += 1
	list.append([maleCount, hivExposedCount, gugulethoCount, mandalayCount, totalCount])

	for i in theIncidents:
		if (i.sequence == '2062' and i.sex == 'Male'):
			maleCount += 1
		if (i.sequence == '2062' and i.hivExposed == 'Yes'):
			hivExposedCount += 1
		if (i.sequence == '2062' and i.site == 'Guguletho'):
			gugulethoCount += 1
		if (i.sequence == '2062' and i.site == 'Mandalay'):
			mandalayCount += 1
		if (i.sequence == '2062'.translate(None, "*~")):
			total += 1
	list.append([maleCount, hivExposedCount, gugulethoCount, mandalayCount, totalCount])

	for i in theIncidents:
		if (i.sequence == '3450' and i.sex == 'Male'):
			maleCount += 1
		if (i.sequence == '3450' and i.hivExposed == 'Yes'):
			hivExposedCount += 1
		if (i.sequence == '3450' and i.site == 'Guguletho'):
			gugulethoCount += 1
		if (i.sequence == '3450' and i.site == 'Mandalay'):
			mandalayCount += 1
		if (i.sequence == '3450'.translate(None, "*~")):
			total += 1
	list.append([maleCount, hivExposedCount, gugulethoCount, mandalayCount, totalCount])

	data = np.array(list)

	fig = plt.figure()
	ax = Axes3D(fig)

	lx= len(data[0])            # Work out matrix dimensions
	ly= len(data[:,0])
	xpos = np.arange(0,lx,1)    # Set up a mesh of positions
	ypos = np.arange(0,ly,1)
	xpos, ypos = np.meshgrid(xpos+0.25, ypos+0.25)

	xpos = xpos.flatten()   # Convert positions to 1D array
	ypos = ypos.flatten()
	zpos = np.zeros(lx*ly)

	dx = 0.5 * np.ones_like(zpos)
	dy = dx.copy()
	dz = data.flatten()

	ax.bar3d(xpos,ypos,zpos, dx, dy, dz, color='b')

	#sh()
	ax.w_xaxis.set_ticklabels(xaxisNames)
	ax.w_yaxis.set_ticklabels(yaxisNames)
	ax.set_xlabel('Category')
	ax.set_ylabel('Serotype')
	ax.set_zlabel('Number of Incidents')

	plt.show()

	return render(request, 'pneumovis/home.html')

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
		messages.success("Upload Successful")

	except Exception as e:
		messages.error(request,"Unable to upload file. "+repr(e))

	return HttpResponseRedirect(reverse("App-adddata"))

def datacards(request):
	return render(request, 'pneumovis/datacards.html')

def help(request):
	return render(request, 'pneumovis/help.html')

def about(request):
	return render(request, 'pneumovis/about.html')
