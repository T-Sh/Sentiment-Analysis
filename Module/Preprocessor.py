import re
import string
import nltk

from Module.Lemmatizer import Lemmatizer
from Module.Stemmer import Stemmer

nltk.download('stopwords')
from nltk.corpus import stopwords


def remove_punctuation(text):
    return re.sub(r'([' + string.punctuation + '])', ' ', text)


def remove_tabs(text):
    text = text.replace("\\n", " ")
    text = text.replace("\\t", " ")
    text = text.replace("\\xa0", " ")
    text = text.replace("\\xc2", " ")

    return text


def to_lower(text):
    return text.lower()


def remove_digits(text):
    return re.sub("[0-9]+", " ", str(text))


class Preprocessor:
    def __init__(self):
        self.stopwords = stopwords.words("russian")
        self.stemmer = Stemmer()
        self.lemmatizer = Lemmatizer()

    def remove_stopwords(self, tokens):
        filtered_tokens = []

        for token in tokens:
            if token not in self.stopwords:
                filtered_tokens.append(token)

        return filtered_tokens

    def lemmatize(self, tokens):
        return self.lemmatizer.process(tokens)

    def stemm(self, tokens):
        return self.stemmer.process(tokens)

    def main_pipeline(self, text):
        text = remove_digits(text)
        text = to_lower(text)
        text = remove_punctuation(text)
        text = remove_tabs(text)

        return text
