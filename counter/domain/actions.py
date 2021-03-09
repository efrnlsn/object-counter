from typing import List

from PIL import Image

from counter.domain.ports import ObjectDetector, ObjectCountRepo
from counter.domain.models import Prediction
from counter.debug import draw
from counter.domain.predictions import over_threshold, count


class CountDetectedObjects:
    def __init__(self, object_detector: ObjectDetector, object_count_repo: ObjectCountRepo):
        self.__object_detector = object_detector
        self.__object_count_repo = object_count_repo

    def execute(self, image, threshold) -> List[Prediction]:
        predictions = self.__find_valid_predictions(image, threshold)
        self.__debug_image(image, predictions)
        object_counts = count(predictions)
        object_classes = list(map(lambda x: x.object_class, object_counts))
        self.__object_count_repo.update_values(object_counts)
        print(self.__object_count_repo.read_values(object_classes))

        return predictions

    @staticmethod
    def __debug_image(image, predictions):
        if __debug__:
            image = Image.open(image)
            draw(predictions, image)

    def __find_valid_predictions(self, image, threshold):
        predictions = self.__object_detector.predict(image)
        predictions = list(over_threshold(predictions, threshold=threshold))
        return predictions
