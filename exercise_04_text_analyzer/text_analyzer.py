import re
from collections import Counter

text = """
Python is easy.
Python is powerful.
Python is everywhere.
"""

def text_analyzer(text):
    
    report = {}

    list_text = re.sub(r'[^\w\s]', '', text).lower().split()
    print(list_text)
    set_text = set(list_text)
    
    report['words'] = len(list_text)
    report['unique_words'] = len(set_text)
    report['most_common'] = Counter(list_text).most_common()[0][0]
    return report

print(text_analyzer(text))