from lib2to3.pgen2 import driver
from pathlib import PosixPath
from turtle import position
from enumerations import DeliveryStatus
from order import Order
from track import Track
from internal import Internal
from position import Position


class Delivery:
    orders: list[Order]
    status: DeliveryStatus
    track: Track
    driver: Internal
    position: Position

    def __init__(self, order:Order, status: DeliveryStatus, track: Track, driver: Internal, position: Position) -> None:
        self.orders.append(order)
        self.status = status
        self.track = track
        self.driver = driver
        self.position = position

    def get_orders(self) -> list[Order]:
        return self.orders

    def set_orders(self, order: Order) -> None:
        self.orders.append(order)

    def get_status(self) -> DeliveryStatus:
        return self.status

    def set_status(self, status: DeliveryStatus) -> None:
        self.status = status

    def get_track(self) -> Track:
        return self.track

    def set_track(self, track: Track) -> None:
        self.track = track

    def get_driver(self) -> Internal:
        return self.driver

    def set_driver(self, driver: Internal) -> None:
        self.driver = driver

    def get_position(self) -> Position:
        return self.position

    def set_position(self, position: Position) -> None:
        self.position = position

    def to_string(self) -> str:
        return f"Status: {self.status}, Track id: {self.track.ID}, Driver: {self.driver.name} {self.last_name}, Position: {self.position.latitude} - {self.position.longitude}"