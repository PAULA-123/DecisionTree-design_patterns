from abc import ABC, abstractmethod
from __future__ import annotations
from typing import List



################################ COMPOSITE ##################################################

# Composite: Estruturas mínimas: Node, DecisionNode, LeafNode.

class Node(ABC):
    """Classe abstrata que define o que todo nó deve possuir"""

    # Não pode ser abstrato, pois os nós folhas não tem filhos
    def add_child():
        pass
    
    @abstractmethod
    def accept(visitor):
        pass

# nós internos (que fazem alguma decisão)
class DecisionNode(Node):
    def __init__(self):
        self.chidren = []

    def add_child():
        pass

    def accept(visitor):
        return super().accept()


# nós folha (resultado final)
class LeafNode(Node):
    def accept(visitor):
        pass


################################ STATE ##################################################

# State: Classe TreeBuilder e estados como SplittingState, StoppingState e  PruningState. 



################################ ITERATOR ##################################################

# Iterator: Um iterador próprio, como PreOrderIterator ou BFSIterator. 



################################ VISITOR ##################################################

# Visitor: Pelo menos dois visitantes independentes, por exemplo: DepthVisitor,  CountLeavesVisitor.