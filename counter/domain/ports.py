from abc import ABC, abstractmethod
from typing import BinaryIO, List, Dict

from counter.domain.models import Prediction, ObjectCount


class ObjectDetector(ABC):
    @abstractmethod
    def predict(self, image: BinaryIO) -> List[Prediction]:
        raise NotImplementedError


class ObjectCountRepo(ABC):
    @abstractmethod
    def update(self, object_counts: List[ObjectCount]) -> Dict[str, ObjectCount]:
        raise NotImplementedError
