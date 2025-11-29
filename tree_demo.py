import tree_design

from tree_design import DecisionTree, DecisionNode, LeafNode, TreeBuilder, SplittingState, StoppingState, PruningState, CountLeavesVisitor, DepthVisitor

builder = TreeBuilder(SplittingState())

builder.build_step()



visitor = CountLeavesVisitor()

for node in tree.iter_bfs():
    node.accept(visitor)