from counter.domain.models import Prediction, Box


def generate_prediction(class_name, score=1.0):
    return Prediction(class_name=class_name, score=score, box=Box(0, 0, 0, 0))