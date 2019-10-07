from Expression import Expression

class ExpressionLogical(Expression):
    def __init__(self, children,operator):
        self.operator = operator
        self.children = children


    def conjonction_and(self,A,B):
        C=[]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i]==B[j]:
                    C.append(A[i])
        return C

    def conjonction_or(self,A,B):
        C=[]
        for i in range(len(A)):
            C.append(A[i])
        for i in range(len(B)):
            if B[i] not in C:
                C.append(B[i])
        return C
    
    def evaluate(self):
        datainput=[]
        data=[]
        for i in range(len(self.children)):
            datainput.append(self.children[i].evaluate())
        if self.operator=='AND':
            output=datainput[0]
            for i in range(1,len(datainput)):
                output=self.conjonction_and(output,datainput[i])
        if self.operator=='OR':
            output=datainput[0]
            for i in range(1,len(datainput)):
                output=self.conjonction_or(output,datainput[i])
        return output
