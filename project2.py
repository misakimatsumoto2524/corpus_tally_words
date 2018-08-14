import os
import codecs
import re
import string as s

def make_set(set):
    word_list = []
    for each in set:
        print(each)
    # print(set)


    # apo_list = {}
    # for i in word_list:
    #     if (i in apo_list.keys()):
    #         apo_list[i] += 1
    #     else:
    #         i = i.lower()
    #         apo_list[i] = 1
    # fix = sorted(apo_list, key=apo_list.get, reverse=True)
    # for i in fix:
    #     print(i + ' ' +str(apo_list[i]))


def clean_text():
    folder = "test"

    for file in os.listdir(folder):
        filepath = os.path.join(folder, file)
        with codecs.open(filepath, "r", encoding='utf-8', errors='ignore') as f:
            content = f.read()
            tag = re.compile("<.*?>")
            punc = re.compile("[^a-zA-Z-' \n]")
            # apos = re.compile("^\'.*\'")

            cleantext = re.sub(tag, '', content)
            cleantext = re.sub(punc, '', cleantext)
            # cleantext = re.sub(apos, '', cleantext)
            cleantext = re.findall(r"\'(.*)+\'|\w| \w+\'+\w| \w+\'", cleantext, re.MULTILINE | re.DOTALL)

    # print(cleantext)

    make_set(cleantext)


clean_text = clean_text()
clean_text
