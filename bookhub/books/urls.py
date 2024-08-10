from django.urls import path
from .views import *

urlpatterns = [
    path('', default_page, name='default'),
    path('search/',search_books, name='search'),
    path('home/',home_page, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('recommendations/',view_recommendations, name='view_recommendations'),
    path('submit/', submit_recommendation, name='submit_recommendation'),
    path('logout/', logout_view, name='logout'),
]
