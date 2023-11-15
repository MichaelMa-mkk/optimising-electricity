import json
from typing import List
from type import *


def parseRoute(filename: str) -> List[Route]:
    routes = json.load(open(filename))
    return [Route(**r) for r in routes['routes']]


def parseVehicle(filename: str) -> List[Vehicle]:
    vehicles = json.load(open(filename))
    return [Vehicle(**v) for v in vehicles['vehicles']]


if __name__ == '__main__':
    for r in parseRoute('./routes.json'):
        assert(type(r) == Route)
    for v in parseVehicle('./vehicles.json'):
        assert(type(v) == Vehicle)