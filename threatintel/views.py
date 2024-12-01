from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Threat
import requests

API_KEY = "caafce8f48mshe698c049de34644p14ad42jsn83c541d8480c"
API_HOST = "public-cloud-threat-intelligence.p.rapidapi.com"

def fetch_threats(request):
    url = f"https://{API_HOST}/threats"
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST,
    }
    response = requests.get(url, headers=headers)
    threats = []

    if response.status_code == 200:
        threats = response.json().get('data', [])

    # Pagination
    paginator = Paginator(threats, 10)  # Show 10 threats per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'threatintel/threats.html', {'page_obj': page_obj})

def save_threat(request, threat_id):
    threat = Threat.objects.filter(threat_id=threat_id).first()
    if not threat:
        url = f"https://{API_HOST}/threats/{threat_id}"
        headers = {
            "X-RapidAPI-Key": API_KEY,
            "X-RapidAPI-Host": API_HOST,
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            threat_data = response.json()
            Threat.objects.create(
                threat_id=threat_id,
                name=threat_data.get('name'),
                description=threat_data.get('description'),
                severity=threat_data.get('severity'),
                bookmarked=True
            )

    return HttpResponseRedirect('/')  # Redirect back to the threats list

def view_bookmarks(request):
    bookmarks = Threat.objects.filter(bookmarked=True)
    return render(request, 'threatintel/bookmarks.html', {'bookmarks': bookmarks})
