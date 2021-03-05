from django.urls import path
from . import views


app_name = 'foods'

urlpatterns = [
    path('home/', views.homePage, name = 'homePage'),
    path('<int:food_id>/', views.detailsPage, name = 'detailsPage'),
    path('about/', views.aboutPage, name = 'aboutPage'),
    path('add/', views.create_item, name = 'create_item'),
    path('update/<int:id>', views.update_item, name = 'update_item'),
    path('delete/<int:id>', views.delete_item, name = 'delete_item'),
]
