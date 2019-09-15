from antlr4 import *
if __name__ is not None and "." in __name__:
    from .frameQLParser import frameQLParser
else:
    from frameQLParser import frameQLParser
from frameQLParserListener import frameQLParserListener
    
class MyListener(frameQLParserListener):
    def __init__(self):
        self.projection_attributes=[]
        self.cross_relations=[]
        self.condition_where=[]
        self.condition_having=[]
        self.group=[]
        self.expression=''
        self.expression_having=''
        self.aggregate=0
        
    def enterTableName(self, ctx:frameQLParser.TableNameContext):
        pass
        #print(ctx.getText())
    
    def enterPredicateExpression(self, ctx:frameQLParser.PredicateExpressionContext):
        self.expression=self.expression+ctx.getText()
        
    def enterLogicalOperator(self, ctx:frameQLParser.LogicalOperatorContext):
        self.expression=self.expression+' '+ctx.getText()+' '
        
    def enterLogicalExpression(self, ctx:frameQLParser.LogicalExpressionContext):
        self.expression=''
        
    def exitLogicalExpression(self, ctx:frameQLParser.LogicalExpressionContext):
        self.condition_where.append(self.expression)

    def enterAggregateWindowedFunction(self, ctx:frameQLParser.AggregateWindowedFunctionContext):
        #print(ctx.getText())
        pass
    def enterExpressionAtomPredicate(self, ctx:frameQLParser.ExpressionAtomPredicateContext):
        #print(ctx.getText())
        pass
    def exitComparisonOperator(self, ctx:frameQLParser.ComparisonOperatorContext):
        if self.aggregate==1:
            self.expression_having=self.expression_having+' '+ctx.getText()+' '
    def enterConstant(self, ctx:frameQLParser.ConstantContext):
        if self.aggregate==1:
            self.expression_having=self.expression_having+ctx.getText()
    def enterFromClause(self, ctx:frameQLParser.FromClauseContext):
        #print(ctx.getText())
        pass
    def enterQuerySpecification(self, ctx:frameQLParser.QuerySpecificationContext):
        #print(ctx.getText())
        pass
    def enterGroupByItem(self, ctx:frameQLParser.GroupByItemContext):
        #print('issou')
        pass
    def enterAggregateFunctionCall(self, ctx:frameQLParser.AggregateFunctionCallContext):
        self.aggregate=1
        self.expression_having=ctx.getText()
    def enterSelectElements(self, ctx:frameQLParser.SelectElementsContext):
        self.projection_attributes.append(ctx.getText())
    def enterTableSources(self, ctx:frameQLParser.TableSourcesContext):
        self.condition_where.append(ctx.getText())
    def enterGroupByItem(self, ctx:frameQLParser.GroupByItemContext):
        self.group.append(ctx.getText())

 
