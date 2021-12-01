from math import sqrt
import logging
from app import travelingproblem


class Problems:
    def __init__(self, locations):
        self.locations = locations
        self.locations_count = len(locations)
        self.distance_matrix = []
        self.solution = "Poblish Problem for Getting the Solution"
        self.num_vehicles = None

    def calculate_distance(self):
        final_list = []
        for p in range(self.locations_count):
            list1 = []
            for q in range(self.locations_count):
                result = sqrt(
                    (self.locations[p][0] - self.locations[q][0]) ** 2 + (
                            self.locations[p][1] - self.locations[p][1]) ** 2)
                list1.append(result)
            final_list.append(list1)
        self.distance_matrix = final_list


class ProblemManager:
    def __init__(self):
        self.next_problem_id = 1
        self.inbound_queues = {}
        self.outbound_queues = {}
        self.subscribed_problems = {}

    def create_problem(self, locations):
        problem_id = self.next_problem_id
        problem = Problems(locations)
        problem.calculate_distance()
        self.inbound_queues[problem_id] = problem
        self.next_problem_id += 1
        logging.info(f"Problem {problem_id} Created.")
        return problem_id, problem

    def subscribe(self):
        problem_ids = list(self.inbound_queues.keys())
        if problem_ids:
            problem_id = min(problem_ids)
            problem = self.inbound_queues[problem_id]
            self.inbound_queues.pop(problem_id)
            self.subscribed_problems[problem_id] = problem
            return problem_id, problem
        logging.warning(f"There is  not any problem to subscribe!")
        return 0, "There is  not any problem to subscribe!"

    def publish(self, problem_id, num_vehicles):
        if self.subscribed_problems.get(problem_id):
            problem = self.subscribed_problems.get(problem_id)
            problem.num_vehicles = num_vehicles
            problem.solution = travelingproblem.main(problem.distance_matrix, num_vehicles)
            self.outbound_queues[problem_id] = problem
            logging.info(f"Problem {problem_id} is Published")
            return problem_id, problem
        else:
            logging.error(f"Problem {problem_id} Does not Subscribed")
            return 0, f"Problem {problem_id} Does not Subscribed"
