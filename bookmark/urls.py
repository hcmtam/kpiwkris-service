from django.urls import path
from . import views


urlpatterns = [
    path("", views.bookmark_result),
    path("list/", views.get_bookmark_list),
    path("bookmark/<str:id>/", views.get_bookmark_by_id),
    path("user/", views.test_create_user),
]
