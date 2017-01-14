# -*- coding: utf-8 -*-
import random
import re
import wolframalpha
import time
import sys
from sys import maxint

from client import jasperpath
WORDS = ["WHO", "WHAT", "HOW MUCH", "HOW MANY", "HOW OLD"]


def handle(text, mic, profile):
    app_id = profile['keys']['WOLFRAMALPHA']
    client = wolframalpha.Client(app_id)

    query = client.query(text)

    result = next(query.results).text

    result = result.encode('ascii', 'ignore')

    if len(result) > 0:
        mic.say(result)
    else:
        mic.say("Sorry, Could you be more specific?.")




def isValid(text):
	return bool(re.search(r'\b(who|what|how|much|many|' +
                          r'old)\b', text, re.IGNORECASE))
