from abc import ABC, abstractmethod
from __future__ import annotations
from typing import List



################################ COMPOSITE ##################################################

# Composite: Estruturas mínimas: Node, DecisionNode, LeafNode.

class Node(ABC):
    """Classe abstrata que define o que todo nó deve possuir"""
    def __init__(self):
        self.children = []
        self._is_leaf = False

    def is_leaf(self) -> bool:
        return self._is_leaf

    @abstractmethod
    def add_child(self, child: Node) -> None:
        pass
    
    @abstractmethod
    def get_children(self)-> List[Node]:
        pass

    @abstractmethod
    def accept(self, visitor)-> None:
        pass

 


# nós internos (que fazem alguma decisão), herda de Node
class DecisionNode(Node):

    def add_child(self, child: Node) -> None:
        self.children.append(child)
        print(f"DecisionNode: nó filho {child} adicionado")

    def get_children(self):
        return self.children

    def accept(self, visitor)-> None:
        visitor.visit_decision_node(self)
        print(f"DecisionNode: Visitor {visitor} aceito")


# nós folha (resultado final), herda de Node
class LeafNode(Node):
    def __init__(self):
        super().__init__()
        self._is_leaf = True


    # Nó folha não pode ter filhos, então levanta um erro
    def add_child(self, child: Node) -> None:
        raise RuntimeError("LeafNode: Nós folhas não podem adicionar filhos!")
    
    def accept(self, visitor)-> None:
        visitor.visit_leaf_node(self)
        print(f"LeafNode: Visitor {visitor} aceito")

    # Retorna lista vázia, já que não tem filhos
    def get_children(self)-> List[Node]:
        return []


################################ STATE ##################################################

# State: Classe TreeBuilder e estados como SplittingState, StoppingState e  PruningState. 



################################ ITERATOR ##################################################

# Iterator: Um iterador próprio, como PreOrderIterator ou BFSIterator. 



################################ VISITOR ##################################################

# Visitor: Pelo menos dois visitantes independentes, por exemplo: DepthVisitor,  CountLeavesVisitor.