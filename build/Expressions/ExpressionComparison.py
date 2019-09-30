from .Expression import Expression

class ExpressionComparison(Expression):
    def __init__(self, leftChild, rightChild,operator):
        self.operator = operator
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.data=[]
        '''
        self.outputleft=[]
        self.outputright=[]
        '''

    def evaluate():
        if type(leftChild)==ExpressionConstant and type(rightChild)==ExpressionTuple:
            attributeRight=self.rightChild.attribute
            if operator=='=':
                for i in range(len(self.rightChild.data)):
                    if self.rightChild.data[i][attributeRight]==self.leftChild:
                        self.data.append(self.rightChild.data[i])
            if operator=='>':
                for i in range(len(self.rightChild.data)):
                    if self.rightChild.data[i][attributeRight]>self.leftChild:
                        self.data.append(self.rightChild.data[i])
            if operator=='<':
                for i in range(len(self.rightChild.data)):
                    if self.rightChild.data[i][attributeRight]<self.leftChild:
                        self.data.append(self.rightChild.data[i])
            if operator=='!=':
                for i in range(len(self.rightChild.data)):
                    if self.rightChild.data[i][attributeRight]!=self.leftChild:
                        self.data.append(self.rightChild.data[i])
        elif type(rightChild)==ExpressionConstant and type(rightLeft)==ExpressionTuple:
            attributeLeft=self.leftChild.attribute
            if operator=='=':
                for i in range(len(self.leftChild.data)):
                    if self.leftChild.data[i][attributeLeft]==self.rightChild:
                        self.data.append(self.leftChild.data[i])
            if operator=='>':
                for i in range(len(self.leftChild.data)):
                    if self.leftChild.data[i][attributeLeft]>self.rightChild:
                        self.data.append(self.leftChild.data[i])
            if operator=='<':
                for i in range(len(self.leftChild.data)):
                    if self.leftChild.data[i][attributeLeft]<self.rightChild:
                        self.data.append(self.leftChild.data[i])
            if operator=='!=':
                for i in range(len(self.leftChild.data)):
                    if self.leftChild.data[i][attributeLeft]!=self.rightChild:
                        self.data.append(self.leftChild.data[i])
        elif type(rightChild)==ExpressionTuple and type(rightLeft)==ExpressionTuple:
            attributeLeft=self.leftChild.attribute
            attributeRight=self.rightChild.attribute
            if operator=='=':
                for i in range(len(self.leftChild.data)):
                    for j in range(len(self.rightChild.data)):
                        if self.leftChild.data[i][attributeLeft]==self.rightChild.data[i][attributeRight]:
                            self.data.append(self.leftChild.data[i])
            if operator=='>':
                for i in range(len(self.leftChild.data)):
                    for j in range(len(self.rightChild.data)):
                        if self.leftChild.data[i][attributeLeft]>self.rightChild.data[i][attributeRight]:
                            self.data.append(self.leftChild.data[i])
            if operator=='<':
                for i in range(len(self.leftChild.data)):
                    for j in range(len(self.rightChild.data)):
                        if self.leftChild.data[i][attributeLeft]<self.rightChild.data[i][attributeRight]:
                            self.data.append(self.leftChild.data[i])
            if operator=='!=':
                for i in range(len(self.leftChild.data)):
                    for j in range(len(self.rightChild.data)):
                        if self.leftChild.data[i][attributeLeft]!=self.rightChild.data[i][attributeRight]:
                            self.data.append(self.leftChild.data[i])
'''
    def evaluate():
        attributeLeft=leftChild.attribute
        attributeRight=rightChild.attribute
        if operator=='=':
            for i in range(len(self.leftChild.data)):
                for j in range(len(self.rightChild.data)):
                    if self.leftChild.data[i][attributeLeft]==self.rightChild.data[j][attributeRight]:
                        self.outputleft.append(self.leftChild.data[i])
                        self.outputright.append(self.rightChild.data[j])
        if operator=='>':
            for i in range(len(self.leftChild.data)):
                for j in range(len(self.rightChild.data)):
                    if self.leftChild.data[i][attributeLeft]>self.rightChild.data[j][attributeRight]:
                        self.outputleft.append(self.leftChild.data[i])
                        self.outputright.append(self.rightChild.data[j])
        if operator=='<':
            for i in range(len(self.leftChild.data)):
                for j in range(len(self.rightChild.data)):
                    if self.leftChild.data[i][attributeLeft]<self.rightChild.data[j][attributeRight]:
                        self.outputleft.append(self.leftChild.data[i])
                        self.outputright.append(self.rightChild.data[j])
        if operator=='!=':
            for i in range(len(self.leftChild.data)):
                for j in range(len(self.rightChild.data)):
                    if self.leftChild.data[i][attributeLeft]!=self.rightChild.data[j][attributeRight]:
                        self.outputleft.append(self.leftChild.data[i])
                        self.outputright.append(self.rightChild.data[j])
'''
