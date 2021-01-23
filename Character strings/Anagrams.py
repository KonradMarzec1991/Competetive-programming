"""
output: {bowel below elbow}, {arc car}, {night thing}, {cried cider}, {act cat}
"""

text = """below the car is a rat drinking cider and bending its elbow while this thing
is an arc that can act like a cat which cried during the night caused by pain in its
bowel"""

import re

RE_PATTERN = re.compile(r'\w+')


def anagrams(S):
    d = {}
    words = RE_PATTERN.findall(S)
    for word in words:
        s = ''.join(sorted(word))
        if s in d:
            d[s].add(word)
        else:
            d[s] = {word}
    return [sorted(list(arr)) for arr in d.values() if len(arr) > 1]


print(anagrams(text))
