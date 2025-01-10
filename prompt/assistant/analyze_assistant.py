from abc import ABCMeta, abstractmethod
from openai import OpenAI
import os

from .prompt import (
    ANALYZE_ASSISTANT_PROMPT,
    ANALYZE_ASSISTANT_FORMAT,
    ENHANCE_ASSISTANT_PROMPT,
    ENHANCE_ASSISTANT_FORMAT,
)


class AnalyzeAssistant(object):
    __metaclass__ = ABCMeta

    status = {}

    def __init__(self):

        self.client = OpenAI(api_key=os.environ["API_KEY"])
        print("init open ai client")

    def extract_keywords(self, requirement, passage):
        # completion = self.client.chat.completions.create(
        #     model="gpt-4o-mini",
        #     messages=[
        #         {"role": "developer", "content": ANALYZE_ASSISTANT_PROMPT},
        #         {"role": "assistant", "content": ANALYZE_ASSISTANT_FORMAT},
        #         {
        #             "role": "user",
        #             "content": {
        #                 "requirement": requirement,
        #                 "passage": passage,
        #             },
        #         },
        #     ],
        # )

        # res = completion.choices[0].message.content
        # print("completion text: ", res)

        res = ANALYZE_ASSISTANT_FORMAT

        return res

    def enhance_passage(self, keywords, passage):
        # completion = self.client.chat.completions.create(
        #     model="gpt-4o-mini",
        #     messages=[
        #         {"role": "developer", "content": ENHANCE_ASSISTANT_PROMPT},
        #         {"role": "assistant", "content": ENHANCE_ASSISTANT_FORMAT},
        #         {
        #             "role": "user",
        #             "content": {
        #                 "keywords": keywords,
        #                 "passage": passage,
        #             },
        #         },
        #     ],
        # )

        # res = completion.choices[0].message.content
        # print("completion text: ", res)

        res = ENHANCE_ASSISTANT_FORMAT

        return res
