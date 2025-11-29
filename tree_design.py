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
        print(f"[DecisionNode]: nó filho {child} adicionado")

    def get_children(self):
        return self.children

    def accept(self, visitor)-> None:
        visitor.visit_decision_node(self)
        print(f"[DecisionNode]: Visitor {visitor} aceito")


# nós folha (resultado final), herda de Node
class LeafNode(Node):
    def __init__(self):
        super().__init__()
        self._is_leaf = True


    # Nó folha não pode ter filhos, então levanta um erro
    def add_child(self, child: Node) -> None:
        raise RuntimeError("[LeafNode]: Nós folhas não podem adicionar filhos!")
    
    def accept(self, visitor)-> None:
        visitor.visit_leaf_node(self)
        print(f"[LeafNode]: Visitor {visitor} aceito")

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
        print(f"[TreeBuilder]: Transition to {State.__class__.__name__}")
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
    """Estado de divisão: cria nós de decisão"""
    
    def handle(self)-> None:
        print(f"[SplittingState]: Dividindo o nó... criando DecisionNode")
        self.tree.transition_to(StoppingState())

class StoppingState(State):
    """Estado de parada: cria nós folha"""
    def  handle(self)-> None:
        print("[StoppingState]: Parando divisão. Criando LeafNode.")
        self.tree.transition_to(PruningState())

class PruningState(State):
    """Estado de poda: remove ou reduz nós"""
    def handle(self):
        print("[PruningState]: Podando a árvore...")
        self.tree.transition_to(SplittingState())



################################ ITERATOR ##################################################

# Iterator: Um iterador próprio, como PreOrderIterator ou BFSIterator. 

class DecisionTree:
    """Define a estrutura da coleção, a árvore de decisão"""
    def __init__(self, root: Node):
        self.root = root

    def __iter__(self):
        return PreOrderIterator(self.root) # Passa a raiz da árvore (coleção)

    def iter_pre_order(self):
        return PreOrderIterator(self.root)

    def iter_bfs(self):
        return  BFSIterator(self.root)
    
class PreOrderIterator:
    """Percorre a árvore em pré-ordem (raiz depois filhos) usando uma pilha."""

    def __init__(self, root: Node):
        print("Criando PreOrderIterator...")
        self.stack = [root]  # começa pela raiz

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration

        # pega o topo da pilha
        node = self.stack.pop()

        print(f"[PreOrderIterator] Visitando nó: {node}")

        # adiciona os filhos na pilha (em ordem inversa)
        # para que o primeiro filho seja visitado primeiro
        for child in reversed(node.get_children()):
            self.stack.append(child)

        return node

class BFSIterator:
    """Percorre a árvore em largura (BFS) usando uma fila."""

    def __init__(self, root: Node):
        print("Criando BFSIterator...")
        self.queue = [root]  # fila começa pela raiz

    def __iter__(self):
        return self

    def __next__(self):
        if not self.queue:
            raise StopIteration

        node = self.queue.pop(0)

        print(f"[Iterator-BFS] Visitando nó: {node}")

        # adiciona os filhos ao final da fila
        for child in node.get_children():
            self.queue.append(child)

        return node
    



################################ VISITOR ##################################################

# Visitor: Pelo menos dois visitantes independentes, por exemplo: DepthVisitor,  CountLeavesVisitor.

class Visitor(ABC):
    """Classe abstrata que define um conjunto de métodos visitantes"""
    @abstractmethod
    def visit_leaf_node(self, leaf_node: LeafNode):
        pass

    @abstractmethod
    def visit_decision_node(self, decision_node: DecisionNode):
        pass


class DepthVisitor(Visitor):
    """Visitor que calcula a  profundidade da árvore. Herda de visitor"""
    def __init__(self):
        self.depth = 0

    def visit_decision_node(self, decision_node: DecisionNode):
        self.depth += 1  
        print(f"[DepthVisitor] Visitando DecisionNode: aumento de profundidade. Profundidade atual: {self.depth}")

    def visit_leaf_node(self, leaf_node: LeafNode):
        print(f"[DepthVisitor] Visitando LeafNode: profundidade final alcançada igual {self.depth})")


class CountLeavesVisitor(Visitor):
    """Visitor que conta o número de folhas da árvore. Herdade visitor"""
    def __init__(self):
        self.leaves = 0

    def visit_leaf_node(self, leaf_node: LeafNode):
        if leaf_node.is_leaf():
            self.leaves+=1
            print(f"[CountLeavesVisitor]Visitando LeafNode: folha encontrada. Total de folhas até o momento: {self.leaves}")

    def visit_decision_node(self, decision_node: DecisionNode):
        print(f"[CountLeavesVisitor] Visitando DecisionNode: Não é nó folha.")




    
    
    