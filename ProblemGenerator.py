import random

class ProblemGenerator:
    def __init__(self,roads):
        self.roads = roads

    def create_search_problems(self):
        dict = {}
        junctions = len(self.roads)
        counter = 0
        while (counter != 100):
            source = random.randint(0, junctions)
            target = self.travel_links(source)
            if (target != source):
                dict[source] = target
                counter += 1
        return dict

    def travel_links(self,source):
        depth = 0
        node = self.roads[source]
        links = node.links
        length = len(links)
        while depth < 50:
            rand = random.randint(0, length - 1)
            target_index = links[rand].target
            node = self.roads[target_index]
            links = node.links
            length = len(links)
            if length == 0:
                return node.index
            depth += 1
        return node.index

    def write_problems_csv(self,dict):
        with open('problems.csv', 'w') as f:
            # string = "source" + ", " + "target"
            # f.write(string)
            # f.write("\n")
            for key, value in dict.items():
                string = str(key) + ", " + str(value)
                f.write(string)
                f.write("\n")




