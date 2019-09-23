from .Expression import Expression

class ExpressionArithmetic(Expression):
    def __init__(self, children=[],operator):
        super().__init__(children)
        self.operator = operator
