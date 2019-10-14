from Expressions.ExpressionComparison import ExpressionComparison
from Expressions.ExpressionConstant import ExpressionConstant
from Expressions.ExpressionTuple import ExpressionTuple
from Expressions.ExpressionLogical import ExpressionLogical
from Expressions.ExpressionArithmetic import ExpressionArithmetic

from Nodes.NodeCondition import NodeCondition
from Nodes.NodeCross import NodeCross
from Nodes.NodeProjection import NodeProjection

data=[[0,50,'bus'],[1,100,'car'],[2,50,'van'],[3,150,'bus'],[4,120,'bus'],[5,130,'car'],[6,250,'bus'],[7,70,'van'],[8,110,'bus']]
'''
for line in data:
    expression1=ExpressionTuple(line,2) #class
    expression2=ExpressionConstant('bus') #bus
    expression3=ExpressionTuple(line,1) #redness
    expression4=ExpressionConstant('100') #100
    expression5=ExpressionComparison([expression1,expression2],'=') #=
    expression6=ExpressionComparison([expression3,expression4],'>') #>
    expression7=ExpressionLogical([expression5,expression6],'AND') #AND
    print(expression7.evaluate())
'''

expression1=ExpressionTuple(2) #class
expression2=ExpressionConstant('bus') #bus
expression31=ExpressionTuple(1)
expression32=ExpressionConstant('30')
expression3=ExpressionArithmetic([expression31,expression32],'-') #redness
expression4=ExpressionConstant('100') #100
expression5=ExpressionComparison([expression1,expression2],'=') #=
expression6=ExpressionComparison([expression3,expression4],'>') #>
expression7=ExpressionLogical([expression5,expression6],'AND') #AND

node1=NodeCross(data)
node2=NodeCondition(node1,expression7)
node3=NodeProjection(node2,[0,2])
print(node3.processing())
'''
for line in data:
    print(expression7.evaluate(line))
'''
