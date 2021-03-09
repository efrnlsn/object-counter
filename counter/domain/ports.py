from abc import ABC, abstractmethod
from typing import BinaryIO, List, Dict

from counter.domain.models import Prediction, ObjectCount


class ObjectDetector(ABC):
    @abstractmethod
    def predict(self, image: BinaryIO) -> List[Prediction]:
        raise NotImplementedError


class ObjectCountRepo(ABC):
    @abstractmethod
    def read_values(self, object_classes: List[str]) -> List[ObjectCount]:
        raise NotImplementedError

    def update_values(self, new_values: List[ObjectCount]):
        raise NotImplementedError
