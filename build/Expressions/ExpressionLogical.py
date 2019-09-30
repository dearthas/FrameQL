from .Expression import Expression

class ExpressionLogical(Expression):
    def __init__(self, leftChild, rightChild,operator):
        self.operator = operator
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.data=[]
        
    def evaluate():
        if operator=='AND':
            for i in range(len(self.leftChild.data)):
                for j in range(len(self.rightChild.data)):
                    if self.leftChild.data[i]==self.leftChild.data[j]:
                        self.data.append(self.leftChild.data[i])
        if operator=='OR':
            for i in range(len(self.leftChild.data)):
                self.data.append(self.leftChild.data[i])
            for i in range(len(self.rightChild.data)):
                self.data.append(self.rightChild.data[i])
