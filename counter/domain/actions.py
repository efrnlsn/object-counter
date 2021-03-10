from typing import List

from PIL import Image

from counter.domain.ports import ObjectDetector, ObjectCountRepo
from counter.domain.models import Prediction, CountResponse
from counter.debug import draw
from counter.domain.predictions import over_threshold, count


class CountDetectedObjects:
    def __init__(self, object_detector: ObjectDetector, object_count_repo: ObjectCountRepo):
        self.__object_detector = object_detector
        self.__object_count_repo = object_count_repo

    def execute(self, image, threshold) -> List[Prediction]:
        predictions = self.__find_valid_predictions(image, threshold)
        object_counts = count(predictions)
        self.__object_count_repo.update_values(object_counts)
        return CountResponse(current_objects=object_counts, total_objects=self.__object_count_repo.read_values())

    @staticmethod
    def __debug_image(image, predictions, image_name):
        if __debug__:
            image = Image.open(image)
            draw(predictions, image, image_name)

    def __find_valid_predictions(self, image, threshold):
        predictions = self.__object_detector.predict(image)
        self.__debug_image(image, predictions, "all_predictions.jpg")
        predictions = list(over_threshold(predictions, threshold=threshold))
        self.__debug_image(image, predictions, f"valid_predictions_with_threshold_{threshold}.jpg")
        return predictions
