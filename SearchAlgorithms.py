from etc.Problem import Problem
from ways import load_map_from_csv
from etc.best_first_graph_search import best_first_graph_search
from etc.ComputingFunc import get_succesors

roads = load_map_from_csv()
from etc.ComputingFunc import h

"""
This function returns the solution for UCS algorithm
given the problem
"""


def find_ucs_rout(source, target, cost_func):
    problem = Problem(source, target, roads)
    solution = best_first_graph_search(problem, cost_func)
    return solution


"""
This function returns the solution for A* algorithm
given the problem
"""


def find_astar_route(source, target, cost_func, heuristic_function):
    problem = Problem(source, target, roads)
    solution = best_first_graph_search(problem, f=lambda node: cost_func(node) + heuristic_function(node))
    return solution


"""
This function returns the solution for IDA* algorithm
given the problem
"""


def find_idastar_route(source, target, cost_func):
    problem = Problem(source, target, roads)
    return IDA_ASTAR(problem, cost_func)


new_limit = 0

"""
The IDA* algorithm learned at tirgul
"""
def IDA_ASTAR(problem, f):
    global new_limit
    new_limit = h(problem.source)
    while True:
        f_limit = new_limit
        new_limit = float("inf")
        solution = DFS_f(problem.source, f, f_limit, problem.target, problem)
        if solution:
            return solution


def DFS_f(source, f, f_limit, target, problem):
    global new_limit
    new_f = f(source) + h(source)
    if new_f > f_limit:
        new_limit = min(new_limit, new_f)
        return None
    if source.index == target:
        return source.get_path()
    succesors = get_succesors(source, problem)
    for succ in succesors:
        solution = DFS_f(succ, f, f_limit, target, problem)
        if solution:
            return solution
        else:
            continue
    return None
