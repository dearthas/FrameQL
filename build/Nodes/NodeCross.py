from .Node import Node

class NodeCross(Node):
    def __init__(self, children=[],relations=[]):
        super().__init__(children)
        self.relations = relations

    def processing(self):
        pass
