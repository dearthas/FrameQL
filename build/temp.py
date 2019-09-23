import sys
from antlr4 import *
from frameQLParser import frameQLParser 
from frameQLLexer import frameQLLexer
from frameQLParserListener import frameQLParserListener
from MyListener import MyListener
from Nodes.NodeProjection import NodeProjection
from Nodes.NodeCondition import NodeCondition
from Nodes.NodeCross import NodeCross


def simple_query_no_aggregate(listener):
    tree=[]
    print(listener.projection_attributes)
    tree.append(NodeProjection(attributes=listener.projection_attributes))
    tree.append(NodeCondition(expressions=listener.condition_where))
    tree.append(NodeCross(relations=listener.cross_relations))
    for i in range(len(tree)-1):
        tree[i].children.append(tree[i+1])
        
def main(argv):
    input_stream = FileStream(argv)
    lexer = frameQLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = frameQLParser(stream)
    tree = parser.root()
    listener = MyListener()
    walker = ParseTreeWalker()
    print(tree.toStringTree(recog=parser))
    walker.walk(listener,tree)
    simple_query_no_aggregate(listener)
    print(listener.logical_expression[0].rightChild.rightChild)
 
if __name__ == '__main__':
    main('test.txt')
