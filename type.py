from typing import List


class Stop:
    def __init__(self, stop_id: str, distance_km: float) -> None:
        self.stop_id, self.distance_km = stop_id, distance_km
    
    def __str__(self) -> str:
        return self.__dict__.__str__()


class Route:
    def __init__(self, route_id: str, stops: dict) -> None:

        self.route_id, self.stops = route_id, [Stop(**s) for s in stops]
        self.total_distance = sum(stop.distance_km for stop in self.stops)

    def __str__(self) -> str:
        return self.__dict__.__str__()


class Vehicle:
    def __init__(self, id: str, capacity_kwh: int, kwh_per_100_km: int) -> None:
        self.id, self.capacity_kwh, self.kwh_per_100_km = id, capacity_kwh, kwh_per_100_km

    def __lt__(self, other) -> bool:
        if self.kwh_per_100_km == other.kwh_per_100_km:
            return self.capacity_kwh / self.kwh_per_100_km < other.capacity_kwh / other.kwh_per_100_km
        else:
            return self.kwh_per_100_km < other.kwh_per_100_km

    def __str__(self) -> str:
        return self.__dict__.__str__()
    
