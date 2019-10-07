from ExpressionComparison import ExpressionComparison
from ExpressionConstant import ExpressionConstant
from ExpressionTuple import ExpressionTuple
from ExpressionLogical import ExpressionLogical

data=[[0,50,'bus'],[1,100,'car'],[2,150,'bus'],[3,50,'van'],[4,120,'bus'],[5,130,'car'],[6,250,'bus']]
expression1=ExpressionTuple(data,2) #class
expression2=ExpressionConstant('bus') #bus
expression3=ExpressionTuple(data,1) #redness
expression4=ExpressionConstant('100') #100
expression5=ExpressionComparison(expression1,expression2,'=') #=
expression6=ExpressionComparison(expression3,expression4,'>') #>
expression7=ExpressionLogical([expression5,expression6],'AND') #AND

print(expression7.evaluate())
