from django.urls import path

from . import views

urlpatterns = [
    # eg: /polls/
    path("", views.IndexView.as_view(), name="index"),
    # eg: /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # eg: /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # eg: /polls/5/vote
    path("<int:pk>/vote/", views.vote, name="vote"),
]