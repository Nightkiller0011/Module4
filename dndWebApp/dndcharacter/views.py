from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import requests
import pyrebase

# Create your views here.

config1={
    "apiKey": "AIzaSyBoE2IiTt8knk_ZD6URPfe4PLLu4xd-djY",
    "authDomain": "cloub-db.firebaseapp.com",
    "databaseURL": "https://cloub-db-default-rtdb.firebaseio.com",
    "projectId": "cloub-db",
    "storageBucket": "cloub-db.appspot.com",
    "messagingSenderId": "509132229826",
    "appId": "1:509132229826:web:29597e8489848dbf5cff5b",
    "measurementId": "G-3XNEM1FKBC"
}
firebase = pyrebase.initialize_app(config1)
authe = firebase.auth()
database=firebase.database()

def mychar(request):
    return render(request, "dndcharacter/display_char.html")

def char2(request):
    return render(request, "dndcharacter/display_char2.html")

def index(request):
    return render(request, 'dndcharacter/index.html', {})