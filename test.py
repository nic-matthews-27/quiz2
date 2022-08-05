from search import Arc, Graph
from math import sqrt



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

        for row in range(len(self.location)):
            if self.location[row][1] == tail_y_coord:
                head_x_coord = self.location[row][0]
                distance = head_x_coord - tail_x_coord

                if distance <= self.radius:
                    arcs.append(Arc(tail, self.location[row], str(tail) + '->' + str(self.location[row]), cost = distance))

            else:
                x_distance = self.location[row][0] - self.location[tail][0]
                y_distance = self.location[row][1] - self.location[tail][1]
                distance = sqrt(x_distance^2 + y_distance^2)
                
                if distance <= self.radius:
                    arcs.append(Arc(tail, self.location[row], str(tail) + '->' + str(self.location[row]),cost = distance))

            

            
graph = LocationGraph(location ={'A': (0, 0), 'B': (3,0), 'C': (3,4), 'D' : (7,0),
}, radius = 5,
   starting_nodes=['A'],
   goal_nodes={'C'}
   )

for arc in graph.outgoing_arcs('A'):
    print(arc)

print()

for arc in graph.outgoing_arcs('B'):
    print(arc)

print()

for arc in graph.outgoing_arcs('C'):
    print(arc)