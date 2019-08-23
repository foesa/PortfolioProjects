from django.urls import path
from . import views

urlpatterns = [
    path("", views.personIndex, name="personIndex"),
    path("<int:pk>/", views.persondetail, name="personDetail"),
    path("search/", views.searchResultsView, name="search_results"),
    path("graph/", views.graphPage, name="graphPage")
]