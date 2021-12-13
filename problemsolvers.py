from app.problemmanager import ProblemManager
import random

pmanager = ProblemManager()


def create_random_problems(n=10):
    for item in range(n):
        location_list = []
        for _ in range(random.randint(2, 20)):
            location_list.append([random.randint(1, 400), random.randint(1, 400)])
        pmanager.create_problem(location_list)
    print( pmanager.inbound_queues)


def create_problem(locations=None):
    print(pmanager.create_problem(locations))


def subscribe():
    print( (pmanager.subscribe()))


def publish(problem_id=1, num_vehicles=1):
    print( pmanager.publish(problem_id, num_vehicles))


def help():
    print("""
    1- create_random_problems(n=10): n is number of problems
    2- create_problem(locations=None): locations is a list of paired locations
    3- subscribe()
    4- publish(problem_id=None, num_vehicles=None)
    5- exit()
    """)




while True:
    cm = input("Please Enter Function Name (Enter help() for getting Function List)")
    try:
        exec(cm)
    except:
        print('Command does not exist')
        help()

