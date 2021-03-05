from typing import List

from PIL import Image

from counter.domain.ports import ObjectDetector
from counter.domain.models import Prediction
from counter.debug import draw
from counter.domain.predictions import over_threshold


class CountDetectedObjects:
    def __init__(self, object_detector: ObjectDetector):
        self.__object_detector = object_detector

    def execute(self, image, threshold) -> List[Prediction]:
        predictions = self.__object_detector.predict(image)
        predictions = list(over_threshold(predictions, threshold=threshold))
        if __debug__:
            image = Image.open(image)
            draw(predictions, image)

        return predictions
