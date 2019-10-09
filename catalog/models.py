from django.db import models

class Benutzer(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=30)

class Infos(models.Model):
    Titel = models.CharField(max_length=20)
    UrlAdresse = models.CharField(max_length=255)
    Benutzername = models.CharField(max_length=15)
    Passwort = models.CharField(max_length=30)
    NachTime = models.BooleanField(default=False)
    InTime = models.BooleanField(default=False)
    Benutzerdefiniert = models.BooleanField(default=False)
    Hours = models.IntegerField()
    Hours2 = models.IntegerField()
    Minutes = models.IntegerField()
    Minutes2 = models.IntegerField()
    FehlschlagAlert = models.BooleanField(default=False)
    ErfolgNachFehlschlagAlert = models.BooleanField(default=False)
    ZuVielFehlschlaege = models.BooleanField(default=False)
    AntwortenSpeichern = models.BooleanField(default=False)
    MyNumber = models.IntegerField()
    MyNumber2 = models.IntegerField()

