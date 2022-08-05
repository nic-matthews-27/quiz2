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
        for row in range(self.location):
            if self.location[row][1] == tail_y_coord:
                head_x_coord = self.location[row][0]
                distance = head_x_coord - tail_x_coord

                if distance <= self.radius:
                    arcs.append(Arc(tail, self.location[row], str(tail) + '->' + str(self.location[row]), distance))

            else:
                x_distance = self.location[row][0] - self.location[tail][0]
                y_distance = self.location[row][1] - self.location[tail][1]
                straight_distance = sqrt(x_distance + y_distance)
                
                if straight_distance <= self.radius:
                    arcs.append(Arc(tail, self.location[row], str(tail) + '->' + str(self.location[row]), distance))

            

            
