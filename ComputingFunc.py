from ways.tools import compute_distance
from ways.info import SPEED_RANGES
from etc.Node import Node

"""
This function returns the succesors of a given node,
with their updated cost depends on the link's max speed.
"""
def get_succesors(node, problem):
    curr_junc = node.junction
    succesors = []
    for link in curr_junc.links:
        max_speed = SPEED_RANGES[link.highway_type][1]
        cost_so_far = node.cost + link.distance / max_speed / 1000
        succ_node = Node(problem.roads[link.target], node, node.get_goal_lat(), node.get_goal_lon(), cost_so_far)
        succesors.append(succ_node)
    return succesors



"""
This cost function returns the current cost of a given node
"""
def g(node):
    return node.get_cost()

"""
This heuristic function returns the estimated cost that
will take a given a node to get to his destination.
The computation computes the distance between the given node's lot and lan
and the destination lot and lan, and divides by the max speed available.
"""
def h(node):
    current_lat = node.junction.lat
    current_lon = node.junction.lon
    goal_lat = node.get_goal_lat()
    goal_lon = node.get_goal_lon()
    distace = compute_distance(current_lat, current_lon, goal_lat, goal_lon)
    return distace / 110
