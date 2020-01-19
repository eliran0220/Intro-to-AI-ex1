import matplotlib.pyplot as plt

"""
This function shows the graph (heuristic cost and actual cost)
given the problem for the 100 A* or 5 IDA* problems generated.
"""
def show_graph(string):
    file = None
    if string == "astar":
        file = open("results/AStarRuns.txt", 'r')
    elif string == "idastar":
        file = open("results/IDAStarRuns.txt", 'r')
    content = file.readlines()
    del content[0]
    for line in content:
        actual, estimated = split_and_arrange(line)
        plt.plot(float(estimated), float(actual), 'ko',markersize=3)
    file.close()
    plt.xlabel("heuristic")
    plt.ylabel("actual")
    plt.show()

"""
This function splits the string to the actual
and estimated cost
"""
def split_and_arrange(string):
    splitted = string.split(",")
    first = splitted[0]
    second = splitted[1]
    second = second.strip("\n")
    return first, second



