from django.urls import path, include

from .views import LatestProductsList

urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
]