from __future__ import annotations
from abc import ABC, abstractmethod
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


class TreeBuilder():
    """Contexto do padrão State. Classe que armazena uma referência a um dos objetos concretos de estado e delega a eles todos os trabalhos específicos de estado."""

    # _state = None # Define o estado atual da árvore

    def __init__(self, State: State)-> None:
        self.transition_to(State)

    def transition_to(self, State: State): 
        # permite alterar o objeto de estado em tempo de execução
        print(f"TreeBuilder: Transition to {State.__class__.__name__}")
        self._state = State
        self._state.tree = self

    def build_step(self): 
        # Método que delega o  comportamento para o estado
        self._state.handle()





class State(ABC):
    """Classe abstrata que define o que todo State deve conter. Também fornece uma referência reversa à árvore do estado anterior"""

    @property
    def tree(self) -> TreeBuilder:
        return self._tree 

    @tree.setter
    def tree(self, tree: TreeBuilder) -> None:
        self._tree = tree  

    @abstractmethod
    def handle(self) -> None:
        pass


class SplittingState(State):
    """fase de divisão: cria decision nodes"""
    
    def handle(self)-> None:
        print(f"SplittingState: Dividindo o nó... criando DecisionNode")
        self.tree.transition_to(StoppingState())

class StoppingState(State):
    """fase de parada: cria leaf nodes"""
    def  handle(self)-> None:
        print("StoppingState: Parando divisão. Criando LeafNode.")
        self.tree.transition_to(PruningState())

class PruningState(State):
    """fase de poda: remove ou reduz nós"""
    def handle(self):
        print("PruningState: Podando a árvore...")
        self.tree.transition_to(SplittingState())



################################ ITERATOR ##################################################

# Iterator: Um iterador próprio, como PreOrderIterator ou BFSIterator. 



################################ VISITOR ##################################################

# Visitor: Pelo menos dois visitantes independentes, por exemplo: DepthVisitor,  CountLeavesVisitor.