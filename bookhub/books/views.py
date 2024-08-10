from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm,RecommendationForm
from .models import Recommendation
from .api import GoogleBooksAPI

api_key = "AIzaSyC98sbEUc2xfNMN9H-xboc8MAa3q6ls3BY"
google_books_api = GoogleBooksAPI(api_key)

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('default')

def search_books(request):
    query = request.GET.get('q', '')
    books = None
    if query:
        try:
            books = google_books_api.fetch_books(query)
        except Exception as e:
            print(f"Error fetching books: {e}")
    return render(request, 'search.html', {'books': books})

def default_page(request):
    return render(request, 'default.html')

@login_required
def home_page(request):
    return render(request, 'home.html')

@login_required
def view_recommendations(request):
    recommendations = Recommendation.objects.all()
    return render(request, 'view_recommendations.html', {'recommendations': recommendations})

@login_required
def submit_recommendation(request):
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            recommendation = form.save(commit=False)
            recommendation.user = request.user
            recommendation.save()
            return redirect('view_recommendations')
        else:
            return render(request, 'submit_recommendation.html', {'form': form})
    else:
        form = RecommendationForm()
    return render(request, 'submit_recommendation.html', {'form': form})
