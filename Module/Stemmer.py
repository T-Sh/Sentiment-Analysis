from nltk.stem import SnowballStemmer
import pandas as pd


class Stemmer:
    def __init__(self):
        self.snowball = SnowballStemmer(language="russian")

    def process(self, tokens):
        stemmed = []

        for token in tokens:
            stemmed.append(self.snowball.stem(token))

        return stemmed

    def show_diff(self, tokens):
        stemmed = self.process(tokens)

        diff_stemming = pd.DataFrame({
            'original': tokens,
            'w/stem': stemmed,
        }, columns=['original', 'with stemming'])

        return diff_stemming
