from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import RegistrationForm
from .models import Bookmark
from .forms import OSINTQueryForm
from django.conf import settings
import requests


API_URL = "https://whatsapp-osint.p.rapidapi.com/endpoint"
API_HEADERS = {
    "X-RapidAPI-Key": settings.API_KEY,
    "X-RapidAPI-Host": settings.API_HOST,
}


@login_required
def search_view(request):
    if request.method == 'POST':
        form = OSINTQueryForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']

            # API Request
            url = "https://whatsapp-osint.p.rapidapi.com/wspic/b64"
            querystring = {"phone": phone_number}
            headers = {
                "x-rapidapi-key": settings.API_KEY,
                "x-rapidapi-host": settings.API_HOST,
            }

            response = requests.get(url, headers=headers, params=querystring)

            # Handle the API response
            if response.status_code == 200:
                try:
                    data = response.json()
                    return render(request, 'osintapp/results.html', {'data': data})
                except ValueError:
                    error_message = "Invalid response from the API."
                    return render(request, 'osintapp/results.html', {'error': error_message})
            else:
                error_message = f"API Error: {response.status_code} - {response.text}"
                return render(request, 'osintapp/results.html', {'error': error_message})
    else:
        form = OSINTQueryForm()

    return render(request, 'osintapp/search.html', {'form': form})

@login_required
def bookmark_result(request):
    if request.method == 'POST':
        query = request.POST.get("query")
        result = request.POST.get("result")
        Bookmark.objects.create(user=request.user, query=query, result=result)
        return redirect('bookmarks')

@login_required
def view_bookmarks(request):
    bookmarks = Bookmark.objects.filter(user=request.user)
    return render(request, 'osintapp/bookmarks.html', {'bookmarks': bookmarks})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('search')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def home_redirect(request):
    return redirect('login')

def home_view(request):
    return render(request, 'osintapp/home.html')

def custom_logout(request):
    logout(request)
    return render(request, 'osintapp/logout.html')