from .Expression import Expression

class ExpressionComparison(Expression):
    def __init__(self, leftChild, rightChild,operator):
        self.operator = operator
        self.leftChild = leftChild
        self.rightChild = rightChild

