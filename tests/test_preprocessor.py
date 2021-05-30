from Module.Lemmatizer import Lemmatizer
from Module.Preprocessor import Preprocessor
from Module.Stemmer import Stemmer
import pytest


def test_lemmatizer():
    lemmatizer = Lemmatizer()
    expected = ["первое", "дважды", "защита"]
    line = ["Первому", "Дважды", "защитой"]
    actual = lemmatizer.process(line)

    assert actual == expected


def test_stemmer():
    stemmer = Stemmer()
    expected = ["перв", "дважд", "защит"]
    line = ["Первому", "Дважды", "защитой"]
    actual = stemmer.process(line)

    assert actual == expected


def test_preprocessor():
    preprocessor = Preprocessor()
    expected = "дважды  два равно   "
    line = "Дважды\\t два Равно \\n4"
    actual = preprocessor.main_pipeline(line)

    assert actual == expected
