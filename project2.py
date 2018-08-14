import os
import codecs
import re
import string as s

def make_set(set):
    apo_list = {}
    word_list = []
    # set = filter("''", set)
    # set = re.split(' |;|,|-|\n', set)
    print(set)

    # for each in set:
    #     # each = re.split(' |;|,|-|\n', each)
    #     # each = list(filter(None, each))
    #     print(each)

    #     for i in each:
    #         if (i in apo_list.keys()):
    #             apo_list[i] += 1
    #         else:
    #             i = i.lower()
    #             apo_list[i] = 1
    # fix = sorted(apo_list)
    # print(fix[0])
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

            # apos = re.compile("^{''.*''}")


            cleantext = re.sub(tag, '', content)
            cleantext = re.sub(punc, '', cleantext)
            cleantext = re.findall("''(.*?)''", cleantext)


    make_set(cleantext)


clean_text = clean_text()
clean_text
