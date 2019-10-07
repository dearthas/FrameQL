from Expression import Expression
from ExpressionConstant import ExpressionConstant
from ExpressionTuple import ExpressionTuple

class ExpressionComparison(Expression):
    def __init__(self, leftChild, rightChild,operator):
        self.operator = operator
        self.leftChild = leftChild
        self.rightChild = rightChild

    def evaluate(self):
        dataright=self.rightChild.evaluate()
        dataleft=self.leftChild.evaluate()
        data=[]
        if type(self.leftChild)==ExpressionConstant and type(self.rightChild)==ExpressionTuple:
            if self.operator=='=':
                for i in range(len(dataright)):
                    if self.rightChild.value(dataright[i])==dataleft:
                        data.append(dataright[i])
            if self.operator=='>':
                for i in range(len(dataright)):
                    if self.rightChild.value(dataright[i])>float(dataleft):
                        data.append(dataright[i])
            if self.operator=='<':
                for i in range(len(dataright)):
                    if self.rightChild.value(dataright[i])<float(dataleft):
                        data.append(dataright[i])
            if self.operator=='!=':
                for i in range(len(dataright)):
                    if self.rightChild.value(dataright[i])!=dataleft:
                        data.append(dataright[i])
            if self.operator=='<=':
                for i in range(len(dataright)):
                    if self.rightChild.value(dataright[i])<=float(dataleft):
                        data.append(dataright[i])
            if self.operator=='>=':
                for i in range(len(dataright)):
                    if self.rightChild.value(dataright[i])>=float(dataleft):
                        data.append(dataright[i])
        elif type(self.rightChild)==ExpressionConstant and type(self.leftChild)==ExpressionTuple:
            if self.operator=='=':
                for i in range(len(dataleft)):
                    if self.leftChild.value(dataleft[i])==dataright:
                        data.append(dataleft[i])
            if self.operator=='>':
                for i in range(len(dataleft)):
                    if self.leftChild.value(dataleft[i])>float(dataright):
                        data.append(dataleft[i])
            if self.operator=='<':
                for i in range(len(dataleft)):
                    if self.leftChild.value(dataleft[i])<float(dataright):
                        data.append(dataleft[i])
            if self.operator=='!=':
                for i in range(len(dataleft)):
                    if self.leftChild.value(dataleft[i])!=dataright:
                        data.append(dataleft[i])
            if self.operator=='>=':
                for i in range(len(dataleft)):
                    if self.leftChild.value(dataleft[i])>=float(dataright):
                        data.append(dataleft[i])
            if self.operator=='<=':
                for i in range(len(dataleft)):
                    if self.leftChild.value(dataleft[i])<=float(dataright):
                        data.append(dataleft[i])
        elif type(self.rightChild)==ExpressionTuple and type(self.leftChild)==ExpressionTuple:
            if self.operator=='=':
                for i in range(len(dataleft)):
                    if self.leftChild.value(dataleft[i])==self.rightChild.value(dataright[i]):
                            data.append(dataleft[i])
            if self.operator=='>':
                for i in range(len(dataleft)):
                    if self.leftChild.value(dataleft[i])>self.rightChild.value(dataright[i]):
                        data.append(dataleft[i])
            if self.operator=='<':
                for i in range(len(dataleft)):
                    if self.leftChild.value(dataleft[i])<self.rightChild.value(dataright[i]):
                        data.append(dataleft[i])
            if self.operator=='!=':
                for i in range(len(dataleft)):
                    if self.leftChild.value(dataleft[i])!=self.rightChild.value(dataright[i]):
                        data.append(dataleft[i])
            if self.operator=='>=':
                for i in range(len(dataleft)):
                    if self.leftChild.value(dataleft[i])>=self.rightChild.value(dataright[i]):
                        data.append(dataleft[i])
            if self.operator=='<=':
                for i in range(len(dataleft)):
                    if self.leftChild.value(dataleft[i])<=self.rightChild.value(dataright[i]):
                        data.append(dataleft[i])
        return data
        
