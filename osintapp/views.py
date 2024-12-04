from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import RegistrationForm
from .models import Bookmark
from .forms import OSINTQueryForm
import requests


API_URL = ""
API_HEADERS = {
    "X-RapidAPI-Key": "",
    "X-RapidAPI-Host": "",
}


@login_required
def search_view(request):
    if request.method == 'POST':
        form = OSINTQueryForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']

            # Make the API call
            response = requests.get(
                API_URL,
                headers=API_HEADERS,
                params={"phone": phone_number}
            )

            # Handle the API response
            if response.status_code == 200:
                data = response.json()  # Parse the JSON response
                return render(request, 'osintapp/results.html', {'data': data})
            else:
                error_message = f"Error: Unable to fetch data. (Status Code: {response.status_code})"
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