"""
This class holds a junction with it's critical info and the cost
to get to it. also saves the parent
"""

class Node:
    def __init__(self, junction, prev,goal_lat,goal_lon, cost):
        self.junction = junction
        self.index = junction.index
        self.prev = prev
        self.cost = cost
        self.goal_lat = goal_lat
        self.goal_lon = goal_lon


    def get_cost(self):
        return self.cost

    def set_cost(self,cost):
        self.cost = cost

    def path_cost(self):
        prev = self.get_prev()
        return prev.cost

    def get_prev(self):
        return self.prev

    def get_goal_lat(self):
        return self.goal_lat

    def get_goal_lon(self):
        return self.goal_lon

    def get_path(self):
        path =[]
        path.insert(0,self)
        prev = self.get_prev()
        while (prev is not None):
            path.insert(0,prev)
            prev = prev.get_prev()
        return path

    def __lt__(self, other):
        if self.get_cost() < other.get_cost():
            return True
        return False

    def __repr__(self):
        return f"{self.index}"