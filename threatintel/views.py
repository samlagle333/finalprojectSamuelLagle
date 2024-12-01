import requests
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Threat

API_KEY = "caafce8f48mshe698c049de34644p14ad42jsn83c541d8480c"
API_HOST = "public-cloud-threat-intelligence.p.rapidapi.com"

@login_required
def fetch_threats(request):
    url = f"https://{API_HOST}/threats"
    headers = {"X-RapidAPI-Key": API_KEY, "X-RapidAPI-Host": API_HOST}
    response = requests.get(url, headers=headers)
    threats = response.json().get('data', []) if response.status_code == 200 else []
    return render(request, 'threatintel/threats.html', {'threats': threats})

@login_required
def save_threat(request, threat_id):
    threat, created = Threat.objects.get_or_create(threat_id=threat_id)
    threat.bookmarked_by.add(request.user)
    return HttpResponseRedirect('/')

@login_required
def view_bookmarks(request):
    bookmarks = Threat.objects.filter(bookmarked_by=request.user)
    return render(request, 'threatintel/bookmarks.html', {'bookmarks': bookmarks})