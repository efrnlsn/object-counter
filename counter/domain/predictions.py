from functools import reduce
from typing import List

from counter.domain.models import Prediction, ObjectCount


def over_threshold(predictions: List[Prediction], threshold: float):
    return filter(lambda prediction: prediction.score >= threshold, predictions)


def count(predictions: List[Prediction]) -> List[ObjectCount]:
    object_classes = map(lambda prediction: prediction.class_name, predictions)
    object_classes_counter = reduce(__count_object_classes, object_classes, {})
    return [ObjectCount(object_class, occurrences) for object_class, occurrences in object_classes_counter.items()]


def __count_object_classes(class_counter: dict, object_class: str):
    class_counter[object_class] = class_counter.get(object_class, 0) + 1
    return class_counter
