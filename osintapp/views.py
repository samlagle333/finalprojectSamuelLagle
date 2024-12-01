import requests
from django.shortcuts import render, redirect
from .models import Bookmark
from .forms import OSINTQueryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegistrationForm

API_URL = "https://whatsapp-osint.p.rapidapi.com/endpoint"
API_HEADERS = {
    "X-RapidAPI-Key": "your-rapidapi-key",
    "X-RapidAPI-Host": "whatsapp-osint.p.rapidapi.com"
}

@login_required
def search_view(request):
    if request.method == "POST":
        form = OSINTQueryForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            response = requests.get(API_URL, headers=API_HEADERS, params={"phone": phone_number})
            data = response.json()
            return render(request, 'osintapp/results.html', {'data': data, 'form': form})
    else:
        form = OSINTQueryForm()
    return render(request, 'osintapp/search.html', {'form': form})

@login_required
def bookmark_result(request):
    if request.method == "POST":
        query = request.POST.get("query")
        result = request.POST.get("result")
        Bookmark.objects.create(user=request.user, query=query, result=result)
        return redirect("bookmarks")

@login_required
def view_bookmarks(request):
    bookmarks = Bookmark.objects.filter(user=request.user)
    return render(request, 'osintapp/bookmarks.html', {'bookmarks': bookmarks})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('search')  # Redirect to your main search page
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})