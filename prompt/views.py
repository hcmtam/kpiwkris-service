from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from operator import itemgetter

# Create your views here.
# request handler / actions

from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .assistant.analyze_assistant import AnalyzeAssistant
from .manager.score_manager import ScoreManager
from .manager.redis_manager import RedisManager


@api_view(["POST"])
def health(request):
    hello = "hhhh"
    return HttpResponse("Hello, World!")


@api_view(["POST"])
def init_user_session(request):
    session, user = itemgetter("sessionId", "user")(request.data)

    return JsonResponse({"sessionId": id})


@api_view(["GET"])
def ask_prompt(request):
    print(request)

    assistant = AnalyzeAssistant()

    print("assistant", assistant)
    answer = assistant.ask_question("Five keys about techinical skills")

    print("from view call assistant class: ", answer)
    return HttpResponse(answer)


@api_view(["POST"])
def find_matched_score(request):
    try:
        body = json.loads(request.body.decode("utf-8"))

        user, requirement, passage, sessionId = itemgetter(
            "user", "requirement", "passage", "sessionId"
        )(body)

        keywords = AnalyzeAssistant().extract_keywords(requirement, passage)

        cal = ScoreManager(keywords).calculate_score()

        score, intersections = itemgetter("score", "intersections")(cal)

        cal["requirement"] = requirement
        cal["passage"] = passage
        cal["user"] = user

        RedisManager().cache_attempt(sessionId, cal)

        return JsonResponse({"score": score, "intersections": intersections})
    except Exception as e:
        return Response({"error": str(e)})


@api_view(["GET"])
def enhance_passage(request):
    try:
        body = json.loads(request.body.decode("utf-8"))

        sessionId = itemgetter("sessionId")(body)

        cache = RedisManager().get_last_attempt(sessionId)

        requirement_words, passage = itemgetter("requirement_words", "passage")(cache)

        result = AnalyzeAssistant().enhance_passage(requirement_words, passage)

        enhancement, passageKeywords = itemgetter("enhancement", "passageKeywords")(
            result
        )

        cal = ScoreManager(
            sessionId, {"requiremnet": requirement_words, "passage": passageKeywords}
        ).calculate_score()

        return JsonResponse({"score": cal["score"], "enhancement": enhancement})
    except Exception as e:
        return Response({"error": str(e)})
