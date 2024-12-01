from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegistrationForm
from .models import Bookmark
from .forms import OSINTQueryForm

@login_required
@login_required
def search_view(request):
    if request.method == 'POST':
        form = OSINTQueryForm(request.POST)
        if form.is_valid():
            # Simulate search result
            result = {"message": "Search completed successfully!"}
            return render(request, 'osintapp/results.html', {'data': result})
    else:
        form = OSINTQueryForm()  # Pass an empty form for GET requests

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