from .Expression import Expression


class ExpressionTuple(Expression):
    def __init__(self,attribute):
        self.attribute = attribute
