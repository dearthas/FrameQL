from Expression import Expression

class ExpressionConstant(Expression):
    def __init__(self,data):
        self.data=data
    def evaluate(self):
        return self.data
    def value(line):
        return self.data
