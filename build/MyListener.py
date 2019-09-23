from antlr4 import *
if __name__ is not None and "." in __name__:
    from .frameQLParser import frameQLParser
else:
    from frameQLParser import frameQLParser
from frameQLParserListener import frameQLParserListener

from Expressions.ExpressionComparison import ExpressionComparison
from Expressions.ExpressionLogical import ExpressionLogical
from Expressions.ExpressionTuple import ExpressionTuple

class MyListener(frameQLParserListener):
    def __init__(self):
        #Build the query plan tree
        self.projection_attributes=[]
        self.cross_relations=[]
        self.condition_where=[]

        #Build the expression tree
        self.comparison_predicate=None
        self.logical_predicate=[]
        self.comparison_number=0
        self.logical_number=0
        self.comparison_expression=[]
        self.logical_expression=[]
        
    def enterLogicalOperator(self, ctx:frameQLParser.LogicalOperatorContext):
        self.logical_expression.append(ExpressionLogical(self.comparison_expression[-1],None,ctx.getText()))


    def enterComparisonOperator(self, ctx:frameQLParser.ComparisonOperatorContext):
        self.comparison_expression.append(ExpressionComparison(self.comparison_predicate,None,ctx.getText()))
        if len(self.comparison_expression)%2==0:
            self.logical_expression[-1].rightChild=self.comparison_expression[-1]


    def enterExpressionAtomPredicate(self, ctx:frameQLParser.ExpressionAtomPredicateContext):
        if self.comparison_predicate is not None:
            self.comparison_predicate=''
            self.comparison_expression[-1].rightChild=ctx.getText()
        else:
            self.comparison_predicate=ctx.getText()

    def enterSelectElements(self, ctx:frameQLParser.SelectElementsContext):
        self.projection_attributes.append(ctx.getText())
    def enterTableSources(self, ctx:frameQLParser.TableSourcesContext):
        self.cross_relations.append(ctx.getText())

 
