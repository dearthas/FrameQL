from .Expression import Expression


class ExpressionTuple(Expression):
    def __init__(self,attribute):
        self.attribute = attribute
    def evaluate(self,Tuple):
        return Tuple
    def value(self,line):
        return line[self.attribute]
