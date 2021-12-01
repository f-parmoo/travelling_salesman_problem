# Travelling Salesman Problem

### This project was implemented with Flask.
### Test was Implemented by Unittest
###Class Names:
- Problems: this class contains each problem attributes like list of locations, distance_matrix and solution for the problem, ....
- ProblemManager: this class manage Inbound and Outbound queues. it contains different queues
  - Attributes
      - inbound_queues: This list contains created problems which are not subscribed. when we create a problem, it will be added to this list. when we subscribe a problem, one problem will be selected and will be sent to user and will be removed from this list (FIFO).
      - subscribed_problems: This list contains subscribed problems. When we subscribe a problem, selected problem will be removed from inbound_queues and will be added to this queue.
      - outbound_queues: This list contains published problems. We can publish problems which are on subscribed_problem list, by publishing we can get the answer and problem will be added to this list.  


      
### API Endpoints:
- /create_problems: We can send list of locations as a Json_Doby input, or all locations will be created randomly
- /subscribe: We can get a problem from Inbound_Queues
- /publish: Method: POST, Json_Body:    {"problem_id" :1,"num_vehicles":2    }
