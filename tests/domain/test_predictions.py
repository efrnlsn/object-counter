from counter.domain.models import Prediction, ObjectCount, Box
from counter.domain.predictions import over_threshold, count


def __generate_prediction(class_name, score=1.0):
    return Prediction(class_name=class_name, score=score, box=Box(0, 0, 0, 0))


def test_filter_predictions_over_threshold() -> None:
    predictions = [__generate_prediction('dog', 0.9),
                   __generate_prediction('cat', 0.8),
                   __generate_prediction('cat', 0.91)]
    good_predictions = over_threshold(predictions, 0.9)
    assert list(good_predictions) == [__generate_prediction('dog', 0.9), __generate_prediction('cat', 0.91)]


def test_count_predictions_by_class() -> None:
    predictions = [__generate_prediction('cat'),
                   __generate_prediction('cat'),
                   __generate_prediction('dog')]
    object_counts = count(predictions)
    assert sorted(object_counts, key=lambda x: x.object_class) == \
        [ObjectCount(object_class='cat', count=2), ObjectCount(object_class='dog', count=1)]
