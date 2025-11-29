import tree_design

from tree_design import TreeBuilder, SplittingState, StoppingState, PruningState

builder = TreeBuilder(SplittingState())

builder.build_step()