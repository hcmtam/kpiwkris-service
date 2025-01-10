from django.urls import path
from . import views


urlpatterns = [
    path("health/", views.health),
    path("ask-prompt/", views.ask_prompt),
    path("matched-score/", views.find_matched_score),
    path("enhance/", views.enhance_passage),
]
