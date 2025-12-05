from tree_design import (
    DecisionNode, LeafNode, DecisionTree,
    DepthVisitor, CountLeavesVisitor,
    TreeBuilder, SplittingState
)


############################## CONSTRUÇÃO DA ÁRVORE  (COMPOSITE) ##########################################

print("\n======================  Testando Composite =====================")

# raiz
root = DecisionNode()

# nível 1
left = DecisionNode()
right = LeafNode()

root.add_child(left)
root.add_child(right)

# nível 2
left.add_child(LeafNode())
left.add_child(LeafNode())

# cria objeto DecisionTree para iterar
tree = DecisionTree(root)



print("\n======================  Testando Iterators =====================")

print("\n--- Pré-Ordem ---")
for node in tree.iter_pre_order():
    print("Visit:", type(node).__name__)

print("\n--- BFS ---")
for node in tree.iter_bfs():
    print("Visit:", type(node).__name__)



print("\n======================  Testando Visitors =====================")

print("\n--- DepthVisitor ---")
depth_visitor = DepthVisitor()

# percorre a árvore chamando accept()
for node in tree.iter_pre_order():
    node.accept(depth_visitor)

print("\nProfundidade final encontrada:", depth_visitor.depth)


print("\n--- CountLeavesVisitor ---")
leaf_visitor = CountLeavesVisitor()

for node in tree.iter_pre_order():
    node.accept(leaf_visitor)

print("Total de folhas:", leaf_visitor.leaves)




print("\n======================  Testando State =====================")

builder = TreeBuilder(SplittingState())

# executa alguns passos do builder
builder.build_step()   # splitting to stopping
builder.build_step()   # stopping to pruning
builder.build_step()   # pruning to splitting

# árvore construída pelo TreeBuilder
generated_tree = builder.get_tree()

print("\n--- Percorrendo árvore gerada pela máquina de estados (BFS) ---")
for node in generated_tree.iter_bfs():
    print("Visit:", type(node).__name__)
