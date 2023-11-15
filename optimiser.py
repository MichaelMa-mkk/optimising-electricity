import dataParser as parser
from typing import List
from type import Vehicle, Route


def computeTotalAndPair(routes: List[Route], vehicles: List[Vehicle]):
    usedVehicle = set() # each vehicle can only be used once
    totalKwh = 0
    vehicleRoutePair = []
    for route in routes:
        assignVehicle = False
        for vehicle in vehicles:
            if vehicle.capacity_kwh / vehicle.kwh_per_100_km * 100 > route.total_distance and not vehicle.id in usedVehicle:
                usedVehicle.add(vehicle.id)
                totalKwh += vehicle.kwh_per_100_km * route.total_distance / 100
                vehicleRoutePair.append((vehicle.id, route.route_id))
                assignVehicle = True
                break
        if not assignVehicle:
            vehicleRoutePair.append(None) # no available vehicle
    return totalKwh, vehicleRoutePair


def optimiseParallel(routes: List[Route], vehicles: List[Vehicle]):
    return computeTotalAndPair(sorted(routes, key=lambda route: route.total_distance, reverse=True), sorted(vehicles))


def optimiseSequential(routes: List[Route], vehicles: List[Vehicle]):
    # return coomputeTotalAndPair(sorted(routes, key=lambda route: route.total_distance, reverse=True), sorted(vehicles, reverse=True))
    totalKwh = 0
    leastEfficientVehicle = sorted(vehicles, reverse=True)[0]
    for route in routes:
        totalKwh += route.total_distance * leastEfficientVehicle.kwh_per_100_km / 100
    return totalKwh, [(leastEfficientVehicle.id, '')]


if __name__ == '__main__':
    routes = parser.parseRoute('./routes.json')
    vehicles = parser.parseVehicle('./vehicles.json')
    resSeq, pairSeq = optimiseSequential(routes, vehicles)
    resPar, pairPar = optimiseParallel(routes, vehicles)
    assert(resSeq >= resPar)
    print(resSeq, pairSeq)
    print(resPar, pairPar)