from django.shortcuts import render


# Create your views here.
from catalog.models import Infos


def index(request) :
	return render(request, 'index.html')

def stringToBoolean(string):
	if string == "on":
		return True
	else:
		return False


def submit(request):
	titel = request.POST.get('titel')
	url = request.POST.get('url')
	benutzername = request.POST.get('benutzername')
	passwort = request.POST.get('passwort')
	benutzerdefiniert = False
	nachtime = False
	intime = False
	myNumber2 = request.POST.get('myNumber2')
	myNumber = request.POST.get('myNumber')
	hours = request.POST.get('hours')
	hours2 = request.POST.get('hours2')
	minutes = request.POST.get('minutes')
	minutes2 = request.POST.get('minutes2')
	ausgewaehltewahl = request.POST.get("a")
	if ausgewaehltewahl == "Wahl1":
		nachtime = True
		myNumber2 = int(request.POST['myNumber2'])
	elif ausgewaehltewahl == "Wahl2":
		intime = True
		hours = int(request.POST['hours'])
		minutes = int(request.POST['minutes'])
	elif ausgewaehltewahl == "Wahl3":
		intime = True
		myNumber = int(request.POST['myNumber'])
		hours2 = int(request.POST['hours2'])
		minutes2 = int(request.POST['minutes2'])
	else:
		benutzerdefiniert = True
	fehlschlagAlert = stringToBoolean(request.POST.get("fehlschlagAlert"))
	erfolgNachFehlschlagAlert = stringToBoolean(request.POST.get("erfolgNachFehlschlagAlert"))
	zuVielFehlschlaege = stringToBoolean(request.POST.get("zuVielFehlschlaege"))
	antwortenSpeichern = stringToBoolean(request.POST.get("antwortenSpeichern"))
	eingabe = Infos(Titel=titel, UrlAdresse=url, Benutzername=benutzername,
					Passwort=passwort, Hours=hours, Hours2=hours2, Minutes=minutes,
					Minutes2=minutes2, FehlschlagAlert=fehlschlagAlert,
					ErfolgNachFehlschlagAlert=erfolgNachFehlschlagAlert,
					ZuVielFehlschlaege=zuVielFehlschlaege, AntwortenSpeichern=antwortenSpeichern,
					MyNumber=myNumber, MyNumber2=myNumber2, Benutzerdefiniert=benutzerdefiniert,
					InTime=intime, NachTime=nachtime,)
	eingabe.save()
	return render(request, 'submit.html', {
		"Titel": titel,
		"UrlAdresse": url,
		"Benutzername": benutzername,
		"Passwort": passwort,
		"Hours": hours,
		"Hours2": hours2,
		"Minutes": minutes,
		"Minutes2": minutes2,
		"FehlschlagAlert": fehlschlagAlert,
		"ErfolgNachFehlschlagAlert": erfolgNachFehlschlagAlert,
		"ZuVielFehlschlaege": zuVielFehlschlaege,
		"AntwortenSpeichern": antwortenSpeichern,
		"MyNumber": myNumber,
		"MyNumber2": myNumber2,
		"Benutzerdefiniert": benutzerdefiniert,
		"InTime": intime,
		"NachTime": nachtime
	})
