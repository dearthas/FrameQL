import sys
from antlr4 import *
from frameQLParser import frameQLParser 
from frameQLLexer import frameQLLexer
from frameQLParserListener import frameQLParserListener
from MyListener import MyListener
import Nodes

def simple_query_with_aggregate(listener):
    tree=[]
    tree.append(Nodes.NodeProjection(attributes=listener.projection_attributes))
    tree.append(Nodes.NodeCondition(expressions=listener.condition_having))
    tree.append(Nodes.NodeGroup(attributes=listener.group))
    tree.append(Nodes.NodeCondition(expressions=listener.condition_where))
    tree.append(Nodes.NodeCross(relations=listener.cross_relations))
    for i in range(len(tree)-1):
        tree[i].children.append(tree[i+1])
    print(tree[0].attributes)
    
def simple_query_no_aggregate(listener):
    tree=[]
    tree.append(Nodes.NodeProjection(attributes=listener.projection_attributes))
    tree.append(Nodes.NodeCondition(expressions=listener.condition_having))
    tree.append(Nodes.NodeCross(relations=listener.cross_relations))
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
    if len(listener.group)>0:
        simple_query_with_aggregate(listener)
    else:
        simple_query_no_aggregate(listener)
 
if __name__ == '__main__':
    main('test.txt')
