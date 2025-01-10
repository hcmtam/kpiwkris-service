from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from operator import itemgetter
import json
from django.core import serializers

from core.models import User, Bookmark
from .redis_manager import RedisManager


@api_view(["POST"])
def test_create_user(request):
    try:

        user = User.objects.create(userEmail="example@example.com", password="password")
        user.save()

        return Response({"status": 200})
    except Exception as e:
        return Response({"error": str(e)})


# Create your views here.
@api_view(["POST"])
def bookmark_result(request):
    try:

        session = itemgetter("sessionId")(request.data)
        cache = RedisManager().get_cache(session)

        user_id = json.loads(cache)["user"]
        user = User.objects.get(userEmail=user_id)

        bookmark = Bookmark.objects.create(user=user, sessionId=session, content=cache)
        bookmark.save()

        return Response({"status": 200})
    except Exception as e:
        return Response({"error": str(e)})


@api_view(["GET"])
def get_bookmark_list(request):
    try:
        userId = request.query_params.get("userId")

        bookmark = Bookmark.objects.filter(user=userId)
        data = list(bookmark.values("id", "sessionName", "sessionId", "createdAt"))

        return Response({"status": 200, "data": data})
    except Exception as e:
        return Response({"error": str(e)})


@api_view(["GET"])
def get_bookmark_by_id(request, id):
    print("get bookmark by id", id)
    try:
        bookmark = Bookmark.objects.get(sessionId=id)
        data = serializers.serialize(
            "json",
            [
                bookmark,
            ],
        )

        data = json.loads(data)[0]["fields"]
        return Response({"status": 200, "data": data})
    except Exception as e:
        return Response({"error": str(e)})
