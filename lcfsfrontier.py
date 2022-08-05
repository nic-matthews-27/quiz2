from search import *

class LCFCFrontier(Frontier){
    
    @abstractmethod
    def add(self, path):
        """Adds a new path to the frontier. A path is a sequence (tuple) of
        Arc objects. You should override this method.

        """

        
    def __iter__(self):
        """We don't need a separate iterator object. Just return self. You
        don't need to change this method."""
        return self

    
    @abstractmethod
    def __next__(self):

        """Selects, removes, and returns a path on the frontier if there is
        any.Recall that a path is a sequence (tuple) of Arc
        objects. Override this method to achieve a desired search
        strategy. If there nothing to return this should raise a
        StopIteration exception.

        """



def print_actions(path):
    """Given a path (a sequence of Arc objects), prints the actions that
    need to be taken and the total cost of those actions. The path is
    usually a solution (a path from the starting node to a goal
    node."""

    if path:
        print("Actions:")
        print(",\n".join("  {}".format(arc.action) for arc in path[1:]) + ".")
        print("Total cost:", sum(arc.cost for arc in path))
    else:
        print("There is no solution!")

}