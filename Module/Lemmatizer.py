import pymorphy2
import pandas as pd


class Lemmatizer:
    def __init__(self):
        self.morph = pymorphy2.MorphAnalyzer()

    def process(self, tokens):
        lemmatized = []

        for token in tokens:
            lemmatized.append(self.morph.parse(token)[0].normal_form)

        return lemmatized

    def show_diff(self, tokens):
        lemmatized = self.process(tokens)

        diff_lemm = pd.DataFrame({
            'original': tokens,
            'w/lemm': lemmatized,
        }, columns=['original', 'w/lemm'])

        return diff_lemm
