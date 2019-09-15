from abc import ABCMeta, abstractmethod

class Node(metaclass=ABCMeta):
    
    @abstractmethod
    def __init__(self, children=[]):
        self.children = children

    @abstractmethod
    def processing(self):
        pass

class NodeProjection(Node):
    def __init__(self, children=[],attributes=[]):
        super().__init__(children)
        self.attributes = attributes

    def processing(self):
        pass

class NodeCondition(Node):
    def __init__(self, children=[],expressions=[]):
        super().__init__(children)
        self.expressions = expressions

    def processing(self):
        pass

class NodeCross(Node):
    def __init__(self, children=[],relations=[]):
        super().__init__(children)
        self.relations = relations

    def processing(self):
        pass

class NodeGroup(Node):
    def __init__(self, children=[],attributes=[]):
        super().__init__(children)
        self.attributes = attributes

    def processing(self):
        pass

class NodeJoing(Node):
    def __init__(self, children=[],expressions=[]):
        super().__init__(children)
        self.expressions = expressions

    def processing(self):
        pass
