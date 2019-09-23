from .Node import Node

class NodeCondition(Node):
    def __init__(self, children=[],expressions=[]):
        super().__init__(children)
        self.expressions = expressions

    def processing(self):
        pass
