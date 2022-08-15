import string
import random
from enumerations import TrackType, TrackStatus


class Track:
    ID: ''.join(random.choice(string.digits) for _ in range(4))
    type: TrackType
    max_weight: float
    current_weight: float
    status: TrackStatus

    def __init__(self, type: TrackType, max_weight: float, current_weight: float, status: TrackStatus) -> None:
        self.type = type
        self.max_weight = max_weight
        self.current_weight = current_weight
        self.status = status
    
    def get_id(self) -> str:
        return self.ID

    def get_type(self) -> TrackType:
        return self.type

    def set_type(self, type: TrackType) -> None:
        self.type = type

    def get_max_weight(self) -> float:
        return self.max_weight

    def set_max_weight(self, max_weight: float) -> None:
        self.max_weight = max_weight

    def get_current_weight(self) -> float:
        return self.current_weight

    def set_current_weight(self, current_weight: float) -> None:
        self.max_weight = current_weight

    def get_status(self) -> TrackStatus:
        return self.status

    def set_status(self, status: TrackStatus) -> None:
        self.status = status

    def toString(self) -> str:
        return f"Id: {self.ID}, Type: {self.type}, Max weight: {self.max_weight}, Current weight: {self.current_weight}, Status: {self.status}"

    
