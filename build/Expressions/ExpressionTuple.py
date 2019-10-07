from Expression import Expression


class ExpressionTuple(Expression):
    def __init__(self,data,attribute):
        self.data = data
        self.attribute = attribute
    def evaluate(self):
        return self.data
    def value(self,line):
        return line[self.attribute]
