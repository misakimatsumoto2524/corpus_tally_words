import os
import codecs
import re

import string as s

def make_set(set):



def clean_text():
    folder = "test"

    for file in os.listdir(folder):
        filepath = os.path.join(folder, file)
        with codecs.open(filepath, "r", encoding='utf-8', errors='ignore') as f:
            content = f.read()
            tag = re.compile('<.*?>')
            punc = re.compile("[^a-zA-Z' ]")
            cleantext = re.sub(tag, '', content)
            cleantext = re.sub(punc, '', cleantext)
            cleantext = cleantext.split(" ")
    print(cleantext)

    make_set(cleantext)


clean_text = clean_text()
clean_text
