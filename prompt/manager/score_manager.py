from abc import ABCMeta, abstractmethod
from openai import OpenAI
import os
from operator import itemgetter

from ..assistant.analyze_assistant import AnalyzeAssistant


class ScoreManager(object):
    __metaclass__ = ABCMeta

    def __init__(self, content):

        requirement, passage = itemgetter("requirementKeywords", "passageKeywords")(
            content
        )

        self.requirement = requirement
        self.passage = passage
        self.score = 0
        self.status = ""

    def calculate_score(self):

        requirement_words = []
        for i in self.requirement:
            requirement_words += self.requirement[i]

        passage_words = []
        for i in self.passage:
            passage_words += self.passage[i]

        intersections = set(requirement_words).intersection(set(passage_words))
        self.score = len(intersections) / len(requirement_words) * 100

        return {
            "score": round(self.score),
            "intersections": list(intersections),
            "requirement_words": list(requirement_words),
        }
