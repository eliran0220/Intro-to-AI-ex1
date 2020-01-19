from ways.tools import compute_distance
from .SearchAlgorithms import find_ucs_rout
from ways.draw import plot_path
from etc.SearchAlgorithms import find_astar_route
from etc.SearchAlgorithms import find_idastar_route
from etc.ComputingFunc import g, h
from etc.Node import Node
import random
from etc.SearchAlgorithms import roads
import csv

"""
This function takes all the generated problems
from the problems.csv file to a dictionary
"""
def problems_to_dict():
    dict = {}
    with open('problems.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            dict[row[0]] = row[1]
    return dict

"""
This function writes the results of each algorithm to a txt file
"""
def write_results(algo):
    if algo == "ucs":
        string = "results/UCSRuns.txt"
        apply_ucs_results(string)
    elif algo == "astar":
        string = "results/AStarRuns.txt"
        apply_astar_results(string)
    elif algo == "idastar":
        string = "results/IDAStarRuns.txt"
        apply_idastar_results(string)

"""
This function is a helper function to write_results
"""
def apply_ucs_results(string):
    # total_time = 0
    with open(string, 'w') as file:
        dict = problems_to_dict()
        for key, value in dict.items():
            file.write("\n")
            source, target = int(key), int(value)
            # start = time.time()
            path = find_ucs_rout(source, target, g)
            # end = time.time()
            cost = path[len(path) - 1].cost
            string = str(cost)
            file.write(string)
            # total_time  = total_time + (end - start)
            # start = 0
            # end = 0
    # average = total_time / 100
    # print(average)

"""
This function is a helper function to write_results
"""
def apply_astar_results(string):
    # total_time = 0
    with open(string, 'w') as file:
        dict = problems_to_dict()
        string = "actual" + ", " + "estimated"
        file.write(string)
        for key, value in dict.items():
            file.write("\n")
            source, target = int(key), int(value)
            # start = time.time()
            path = find_astar_route(source, target, g, h)
            # end = time.time()
            cost = path[len(path) - 1].cost
            finish_node = roads[target]
            start_node = Node(roads[source], None, finish_node.lat, finish_node.lon, 0)
            estimated_cost = h(start_node)
            string = str(cost) + ", " + str(estimated_cost)
            file.write(string)
            #total_time = total_time + (end - start)
            # start = 0
            # end = 0
    # average = total_time / 100
    # print(average)

"""
This function is a helper function to write_results
"""
def apply_idastar_results(string):
    #total_time = 0
    with open(string, 'w') as file:
        dict = choose_problems_for_idastar()
        string = "actual" + ", " + "estimated"
        file.write(string)
        for key, value in dict.items():
            file.write("\n")
            source, target = int(key), int(value)
            #start = time.time()
            path = find_idastar_route(source, target, h)
            #end = time.time()
            cost = path[len(path) - 1].cost
            finish_node = roads[target]
            start_node = Node(roads[source], None, finish_node.lat, finish_node.lon, 0)
            estimated_cost = h(start_node)
            string = str(cost) + ", " + str(estimated_cost)
            file.write(string)
            #total_time = total_time + (end - start)
            #start = 0
            #end = 0
    #average = total_time / 5
    #print(average)

"""
This function is using the compute_distance for the algorithms
"""
def compute_estimated(source, target):
    start_lat = roads[source].lat
    start_lon = roads[source].lon
    finish_lat = roads[target].lat
    finish_lon = roads[target].lon
    distance = compute_distance(start_lat, start_lon, finish_lat, finish_lon)
    return distance

"""
This function is a helper function to choose 5 problems to ida*
"""
def choose_problems_for_idastar():
    dict = {6725: 6729, 88121: 88123, 650840: 650845, 732431: 732436, 244723: 244725}
    return dict
    # 6725 = 6729  # problem 5
    # 88121 = 88123  # problem 100
    # 650840 = 650845  # problem 93
    # 732431 = 732436 # problem 1
    # 244723 = 244725  # problem 50


def get_indexes(path):
    list = []
    for node in path:
        list.append(int(node.index))
    return list

"""
This function is for drawing the path for the A* algorithm for 10
random problems
"""
def draw_path():
    random_problems = random.sample(range(1, 100), 10)
    dict = problems_to_dict()
    for problem in random_problems:
        source = list(dict)[problem]
        target = dict[source]
        path = find_astar_route(int(source), int(target), g, h)
        junctions = get_indexes(path)
        plot_path(roads, junctions, 'g')
