import os
import codecs
import numpy as np

# folder path to read files
folder = "test"
def project2():
    for file in os.listdir(folder):
        filepath = os.path.join(folder, file)
        with codecs.open(filepath, "r", encoding='utf-8', errors='ignore') as f:
            content = f.readlines()
            for piece in content:
                if ("<" in piece):
                    index_start = piece.index("<")
                    index_end = piece.index(">") + 1
                    piece = piece[:index_start] + piece[index_end:]
                print(piece)



project2 = project2()
project2
