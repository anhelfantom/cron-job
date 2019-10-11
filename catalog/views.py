from django.shortcuts import render
from catalog.models import Infos
from catalog.models import Benutzer
from django.urls import reverse
from django.http import HttpResponseRedirect


def main(request):
	return HttpResponseRedirect(reverse("cron:index", args=(0,)))

def login(request, Account=1):
	return render(request, 'login.html', {'Account': Account})

def register(request, Account=0):
	return render(request, 'login.html', {'Account': Account})

def tryLogin(request):
	loginName = request.POST['login_name']
	loginPassword = request.POST['login_password']
	try:
		benutzer_data = Benutzer.objects.get(username=loginName)
	except(KeyError, Benutzer.DoesNotExist):
		return render(request, 'login.html', {
			'warnung_nachricht': "Dein Passwort oder Benutzername sind nicht korrekt",
			'Account': 1,
			'login_name': loginName,
			'login_password': loginPassword
		})
	else:
		richtige_password = benutzer_data.password
		if richtige_password != loginPassword:
			return render(request, 'login.html', {
				'warnung_nachricht': "Dein Passwort oder Benutzername sind nicht korrekt",
				'Account': 1,
				'login_name': loginName,
				'login_password': loginPassword
			})
		else:
			request.session['LoggedIn'] = True
			request.session['username'] = loginName
			request.session.set_expiry(0)
			return HttpResponseRedirect(reverse('cron:index', args=(0,)))

def tryRegister(request):
	loginName = request.POST.get('login_name')
	loginPassword = request.POST.get('login_password')
	try:
		benutzer_data = Benutzer.objects.get(username=loginName)
	except(KeyError, Benutzer.DoesNotExist):
		eingabe = Benutzer(username=loginName, password=loginPassword)
		eingabe.save()
		return HttpResponseRedirect(reverse('cron:login'))
	else:
		return render(request, 'login.html', {
			'warnung_nachricht': "Diese Benutzername existiert bereits",
			'Account': 0,
			'login_name': loginName,
			'login_password': loginPassword
		})


def index(request, enabled=0):
	if request.session.get('LoggedIn', False):
		return render(request, 'index.html', {
			"enabled": enabled,
			"error": ""
		})
	else:
		return render(request, 'login.html', {
			'warnung_nachricht': "Bitte einloggen",
			'Account': 1
		})


def stringToBoolean(string):
	if string == "on":
		return True
	else:
		return False

def login(request, enabled=0):
	if request.session.get('LoggedIn', False):
		return render(request, 'index.html', {
			"enabled": enabled,
			"error": ""
		})
	else:
		return render(request, 'login.html', {
			'warning_nachricht': "Können Sie sich bitte einloggen",
			'Account': 1
		})


def submit(request, enabled=0):
	if request.session.get('LoggedIn', False):
		titel = request.POST.get('titel')
		url = request.POST.get('url')
		myNumber2 = request.POST.get('myNumber2')
		myNumber = request.POST.get('myNumber')
		hours = request.POST.get('hours')
		benutzerdefiniert = False
		requiredhttp = bool(enabled)
		Wahl1 = False
		Wahl2 = False
		Wahl3 = False
		Wahl4 = False
		hours2 = request.POST.get('hours2')
		minutes = request.POST.get('minutes')
		minutes2 = request.POST.get('minutes2')
		fehlschlagAlert = stringToBoolean(request.POST.get("fehlschlagAlert"))
		erfolgNachFehlschlagAlert = stringToBoolean(request.POST.get("erfolgNachFehlschlagAlert"))
		ausgewaehltewahl = request.POST.get("a")
		if ausgewaehltewahl == "Wahl1":
			Wahl1 = True
			myNumber2 = int(request.POST['myNumber2'])
		elif ausgewaehltewahl == "Wahl2":
			Wahl2 = True
			hours = int(request.POST['hours'])
			minutes = int(request.POST['minutes'])
		elif ausgewaehltewahl == "Wahl3":
			Wahl3 = True
			myNumber = int(request.POST['myNumber'])
			hours2 = int(request.POST['hours2'])
			minutes2 = int(request.POST['minutes2'])
		else:
			Wahl4 = True
			benutzerdefiniert = True
		zuVielFehlschlaege = stringToBoolean(request.POST.get("zuVielFehlschlaege"))
		antwortenSpeichern = stringToBoolean(request.POST.get("antwortenSpeichern"))
		if requiredhttp:
			benutzername = request.POST.get('benutzername')
			passwort = request.POST.get('passwort')
			try:
				benutzer_data = Benutzer.objects.get(username=benutzername)
			except(KeyError, Benutzer.DoesNotExist):
				return render(request, 'index.html', {
					"enabled": enabled,
					"warnung": "Sie können nicht ein Cron Job für einen anderen Benutzer machen"
				})
			else:
				richtige_password = benutzer_data.password
				if richtige_password != passwort:
					return render(request, 'index.html', {
						"enabled": enabled,
						"warning": "Sie können nicht ein Cron Job für einen anderen Benutzer machen"
					})
		else:
			benutzername = ""
			passwort = ""
		eingabe = Infos(Titel=titel, UrlAdresse=url, Benutzername=benutzername,
						Passwort=passwort, Hours=hours, Hours2=hours2, Minutes=minutes,
						Minutes2=minutes2, FehlschlagAlert=fehlschlagAlert,
						ErfolgNachFehlschlagAlert=erfolgNachFehlschlagAlert,
						ZuVielFehlschlaege=zuVielFehlschlaege, AntwortenSpeichern=antwortenSpeichern,
						MyNumber=myNumber, MyNumber2=myNumber2, Benutzerdefiniert=benutzerdefiniert)
		eingabe.save()
		return render(request, 'submit.html', {
							"Titel": titel,
							"Wahl1":Wahl1,
							"Wahl2":Wahl2,
							"Wahl3":Wahl3,
							"Wahl4":Wahl4,
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
							"Benutzerdefiniert": benutzerdefiniert})
	else:
		return render(request, 'login.html', {
			'warning_nachricht': "Bitte Einloggen",
			'Account': 1
		})