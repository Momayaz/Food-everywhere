from django.urls import path
from . import views


app_name = 'foods'

urlpatterns = [
    path('home/', views.homePage, name = 'homePage'),
    path('<int:food_id>/', views.detailsPage, name = 'detailsPage'),
    path('about/', views.aboutPage, name = 'aboutPage')
]
