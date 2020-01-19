from etc.Node import Node
class Problem:
    def __init__(self,source,target,roads):
        self.source = Node(roads[source],None,roads[target].lat,roads[target].lon,0)
        self.target = target
        self.roads = roads

