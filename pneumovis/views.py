from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'pneumovis/home.html')

def adddata(request):
    return render(request, 'pneumovis/adddata.html')

def datacards(request):
    return render(request, 'pneumovis/datacards.html')

def help(request):
    return render(request, 'pneumovis/help.html')

def about(request):
    return render(request, 'pneumovis/about.html')

def upload_csv(request):
	data = {}
	if "GET" == request.method:
		return render(request, "myapp/upload_csv.html", data)
    # if not GET, then proceed
	try:
		csv_file = request.FILES["csv_file"]
		if not csv_file.name.endswith('.csv'):
			messages.error(request,'File is not CSV type')
			return HttpResponseRedirect(reverse("myapp:upload_csv"))

		file_data = csv_file.read().decode("utf-8")

		lines = file_data.split("\n")
        titles = lines[0].split(",")
        if (titles[0] != "participantID" or titles[1] != "npa_a4_growth"
            titles[2] != "dateCollected" or titles[3] != "presence"
            titles[4] != "dob" or titles[5] != "sex"
            titles[6] != "hivExposed" or titles[7] != "site"
            titles[8] != "serotype" or titles[9] != "vaccine" or titles[10] != "sequence"):
            messages.error(request,'CSV file is not in corrrect format, please check the format above and try again')
			return HttpResponseRedirect(reverse("myapp:upload_csv"))

		#loop over the lines and save them in db. If error , store as string and then display
		for line in lines:
			fields = line.split(",")
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

			newIncident = new Incident(participantID=participantID, npa_a4_growth=npa_a4_growth, dateCollected=dateCollected, presence=presence, dob=dob,sex=sex,
                                        hivExposed=hivExposed, site=site, serotype=serotype, vaccine=vaccine, sequence=sequence)
            newIncident.save()

	except Exception as e:
		messages.error(request,"Unable to upload file. "+repr(e))

	return HttpResponseRedirect(reverse("myapp:upload_csv"))
