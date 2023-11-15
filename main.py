import dataParser as parser
from optimiser import optimiseParallel, optimiseSequential
import json


def outputResult(pairs, resultSeq, resultPar) -> None:
    json.dump({
        'vehicle_route_pairs': pairs,
        'total_kwh_with_least_efficient_vehicle': resultSeq,
        'total_kwh_with_optimal_vehicle_route_pairs': resultPar,
    },
    open('./result.json', 'w'))


if __name__ == '__main__':
    routes = parser.parseRoute('./routes.json')
    vehicles = parser.parseVehicle('./vehicles.json')
    resultSeq, _ = optimiseSequential(routes, vehicles)
    resultPar, vehicleRoutePairs = optimiseParallel(routes, vehicles)
    outputResult(vehicleRoutePairs, resultSeq, resultPar)