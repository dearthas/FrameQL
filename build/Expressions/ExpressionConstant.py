from .Expression import Expression

class ExpressionConstant(Expression):
    def __init__(self,data):
        self.data=data
