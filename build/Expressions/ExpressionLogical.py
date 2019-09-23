from .Expression import Expression

class ExpressionLogical(Expression):
    def __init__(self, leftChild, rightChild,operator):
        self.operator = operator
        self.leftChild = leftChild
        self.rightChild = rightChild
