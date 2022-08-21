class Position:
    latitude: float
    longitude: float

    def __init__(self, latitude: float, longitude: float) -> None:
        self.latitude = latitude
        self.longitude = longitude

    def get_latitude(self) -> float:
        return self.latitude

    def set_latitude(self, latitude: float) -> None:
        self.latitude = latitude

    def get_longitude(self) -> float:
        return self.longitude

    def set_longitude(self, longitude: float) -> None:
        self.longitude = longitude

    def to_string(self) -> str:
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}"

    
