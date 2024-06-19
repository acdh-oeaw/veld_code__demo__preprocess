# veld_code__demo__preprocess

### what is it?

This is a demo veld code repo. It contains code that is mainly intended to be integrated into a veld
chain, but can also be run on its own, by defaulting to the `data` folder.

### what does it do?

It simply downloads the bible, and prepares it for word2vec training (removes newlines, makes all
text lower-case, splits the data into sentences, and saves it as a file with each line being a
sentence).

