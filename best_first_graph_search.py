from etc import Pq
from etc.ComputingFunc import get_succesors

"""
The implementation of best first search for a graph, for the
UCS and A* algorithm (given the f function)
"""


def best_first_graph_search(problem, f):
    frontier = Pq.PriorityQueue(f)
    node = problem.source
    frontier.append(node)
    closed_list = set()
    while frontier:
        node = frontier.pop()
        if node.index == problem.target:
            return node.get_path()
        closed_list.add(node.index)
        succesors = get_succesors(node, problem)
        for succ in succesors:
            if succ.index not in closed_list and succ not in frontier:
                frontier.append(succ)
            elif succ in frontier and f(succ) < frontier[succ]:
                del frontier[succ]
                frontier.append(succ)

    return None
