from search import Arc, Graph
from math import sqrt
from collections import OrderedDict



class LocationGraph(Graph):
    def __init__(self, location, radius, starting_nodes, goal_nodes):
        self.location = location
        self.radius = radius
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes
    
    def starting_nodes(self):
        return self._starting_nodes
    
    def is_goal(self, node):
        if node == self.goal_nodes:
            return True
    
    def outgoing_arcs(self, tail):
        tail_y_coord = self.location[tail][1]
        tail_x_coord = self.location[tail][0]
        arcs = []
        
        for row in self.location:

            if self.location[row][1] == tail_y_coord:
                head_x_coord = self.location[row][0]
                distance = abs(float(head_x_coord - tail_x_coord))

                if distance <= self.radius:
                    if self.location[row] != self.location[tail]:
                        arcs.append(Arc(tail, row, str(tail) + '->' + row, cost = distance))

            else:
                x_distance = self.location[row][0] - self.location[tail][0]
                y_distance = self.location[row][1] - self.location[tail][1]
                distance = abs(sqrt(x_distance**2 + y_distance**2))
                
                if distance <= self.radius:
                   arcs.append(Arc(tail, row, str(tail) + '->' + str(row),cost = distance))

        sorted_arcs = sorted(arcs)
        return sorted_arcs
            

            
graph = LocationGraph(
    location={'SW': (-2, -2),
              'NW': (-2, 2),
              'NE': (2, 2),
              'SE': (2, -2)},
    radius = 5,
    starting_nodes=['NE'],
    goal_nodes={'SW'}
)

for arc in graph.outgoing_arcs('NE'):
    print(arc)

print()

for arc in graph.outgoing_arcs('NW'):
    print(arc)

print()

for arc in graph.outgoing_arcs('SW'):
    print(arc)

print()


for arc in graph.outgoing_arcs('SE'):
    print(arc)