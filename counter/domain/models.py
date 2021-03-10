from dataclasses import dataclass
from typing import List


@dataclass
class Box:
    xmin: float
    ymin: float
    xmax: float
    ymax: float


@dataclass
class Prediction:
    class_name: str
    score: float
    box: Box


@dataclass
class ObjectCount:
    object_class: str
    count: int


@dataclass
class CountResponse:
    current_objects: List[ObjectCount]
    total_objects: List[ObjectCount]
