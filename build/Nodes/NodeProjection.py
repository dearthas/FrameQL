from .Node import Node

class NodeProjection(Node):
    def __init__(self, children=[],attributes=[]):
        super().__init__(children)
        self.attributes = attributes

    def processing(self):
        pass
