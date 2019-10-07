from Expression import Expression

class ExpressionArithmetic(Expression):
    def __init__(self,data,children=[],operator):
        self.operator = operator
        self.children=children
        self.data=data

    def evaluate():
        return data
    def value(line):
        if operator=='+':
            for i in range(len(self.children)):
                somme=somme+self.children[i].value(line)
                return somme
        if operation=='-':
            return self.children[0].value(line)-self.children[1].value(line)
        if operation=='*':
            return self.children[0].value(line)*self.children[1].value(line)
        if operation=='/':
            return self.children[0].value(line)/self.children[1].value(line)
