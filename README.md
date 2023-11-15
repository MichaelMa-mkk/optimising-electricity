# Optimising electricity consumption

Welcome to the Delivery Emissions live coding exercise for HIVED, the eco-friendly delivery company :truck::recycle:

At HIVED, we will never use fossil fuels, so all our vans are electric. :zap:
But different sizes of vans will vary in their electricity consumption, and so it's better for the planet (and for our wallet! :money_with_wings:) to carefully select which vans are used for which delivery routes.

## Exercise

We'd like you to write a program that assigns vehicles to routes, in a way that will minimise electricity consumption (in kWh).

### Input

1. `routes.json` This contains an array of different routes. Each route will have an ID and a list of stops. Each stop will have a distance from the previous stop in kilometers.

2. `vehicles.json` This contains an array of vehicles. Each vehicle will have an ID, a capacity in kWh, and an average electricity consumption in kWh/100km.

### Output

As an output, we'd like to see:

- The list of optimal vehicle-route pairs
- The total kWh required to complete all routes sequentially using the least efficient vehicle only
- The total kWh required to complete all routes in parallel using the optimal vehicle-route pairs

## Instructions

### For live sessions

- :speech_balloon: See this exercise as an interactive session, ask us questions as you would if we were working together
- :ok_hand: Aim to write code in the way you would every day - **you will not be penalised if you don't complete the exercise**

### For take-homes

- :pencil2: Feel free to reach out to ask for clarifications and document your assumptions
- :ok_hand: Aim to write code in the way you would every day - we expect you to complete the exercise

## Solution

### Result

`result.json` This contains

- `vehicle_route_pairs`: The list of optimal vehicle-route pairs
- `total_kwh_with_least_efficient_vehicle`: The total kWh required to complete all routes sequentially using the least efficient vehicle only  
  _assumption:_ This result is calculated by using the least efficient vehicle on each route. The purpose of the result is to show the worst case of electricity consumption
- `total_kwh_with_optimal_vehicle_route_pairs`: The total kWh required to complete all routes in parallel using the optimal vehicle-route pairs

### Run

```
python3 main.py
```

For module test, run each module separately

```
python3 dataParser.py
python3 optimiser.py
```

### Code

- `type.py` This contains definition and declaration of Python Objects `Stop`, `Route`, and `Vehicle`, which corresponds to the data structure defined in **Input**.
- `dataParser.py` This contains parser to load json data and translate to Python Objects.
- `optimiser.py` This contains optimiser to compute the optimal vehicle-route pairs and the corresponding kWh required in total.
- `main.py` This contains function to load the json data from `data` directory, run optimiser to compute the optimal result, and generate `result.json` to output the result
