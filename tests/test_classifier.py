import pytest

from Module.Classifier import Classifier


def test_classifier():
    classifier = Classifier()
    expected = ["NEUTRAL", "POSITIVE", "NEGATIVE"]
    actual = []
    for i in range(3):
        actual.append(classifier.convert_id_to_sentiment(str(i)))

    assert actual == expected
