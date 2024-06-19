# veld_code__demo__preprocess

This is a demo veld code repo. It contains code that is mainly intended to be integrated into a veld
chain, but can also be run on its own, by defaulting to the `data` folder.

This code simply downloads a txt file from a given url parameter, and prepares it for word2vec
training (removes newlines, makes all text lower-case, splits the data into sentences, and saves it
as a file with each line being a sentence).

