import os
import nltk
import requests
from nltk.tokenize import sent_tokenize


OUT_FILE = "/veld/output/" + os.getenv("out_file")


# load sentence splitting function
nltk.download('punkt')


# download and process text
content = requests.get("https://github.com/mxw/grmr/raw/master/src/finaltests/bible.txt").text
content = content.lower()
content = content.replace("\r\n", " ")
content = sent_tokenize(content)


# write to file, one sentence per line
with open(OUT_FILE, "w") as f:
    for line_nr, sentence in enumerate(content):
        f.write(sentence + "\n")
        # from line 29810 onwards, there is only gutenberg metadata left, so break the loop
        if line_nr == 29809:
            break

