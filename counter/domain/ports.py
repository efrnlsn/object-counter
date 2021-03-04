from abc import ABC, abstractmethod
from typing import BinaryIO, List

from counter.domain.models import Prediction


class ObjectDetector(ABC):
    @abstractmethod
    def predict(self, image: BinaryIO) -> List[Prediction]:
        raise NotImplementedError
