from deeppavlov import build_model
import torch


# Don't forget changing of path in config!
class Classifier:
    def __init__(self, path='../config.json'):
        self.model = build_model(path)
        self.sentiment_map = {"0": "NEUTRAL", "1": "POSITIVE", "2": "NEGATIVE"}

    def convert_id_to_sentiment(self, id_num):
        if id_num not in self.sentiment_map:
            raise TypeError("Unknown sentiment ID")

        return self.sentiment_map[id_num]

    @torch.no_grad()
    def predict(self, inputs, return_class=True):
        predicted = self.model([inputs])
        if return_class:
            predicted = self.convert_id_to_sentiment(predicted[0])
        return predicted
