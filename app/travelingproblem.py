from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


def create_data_model(geo_locations, num_vehicles=1):
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = geo_locations
    data['num_vehicles'] = num_vehicles
    data['depot'] = 0
    return data



def print_solution( manager, routing, solution, num_vehicles):
    plan_output = ''
    for vehicle_id in range(num_vehicles):
        index = routing.Start(vehicle_id)
        plan_output += f'     Route VehicleID({vehicle_id})'
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += ' {} ->'.format(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle (previous_index, index, vehicle_id)
        plan_output += ' {}   '.format(manager.IndexToNode(index))
        plan_output += 'Route distance: {}miles'.format(route_distance)
    return plan_output


def main(geo_location, num_vehicles):
    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model(geo_location , num_vehicles)

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.

    if solution:
        return  print_solution( manager, routing, solution ,data['num_vehicles'] )
    return None



