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
        object_counts = count(predictions)
        object_classes = list(map(lambda x: x.object_class, object_counts))
        self.__object_count_repo.update_values(object_counts)
        print(self.__object_count_repo.read_values(object_classes))

        return predictions

    @staticmethod
    def __debug_image(image, predictions, image_name):
        if __debug__:
            image = Image.open(image)
            draw(predictions, image, image_name)

    def __find_valid_predictions(self, image, threshold):
        predictions = self.__object_detector.predict(image)
        self.__debug_image(image, predictions, "all_predictions.jpg")
        predictions = list(over_threshold(predictions, threshold=threshold))
        self.__debug_image(image, predictions, "valid_predictions.jpg")
        return predictions
