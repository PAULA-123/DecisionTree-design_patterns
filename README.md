#  Projeto Individual de Modelagem — Árvore de Decisão (Mock)

Este projeto apresenta a modelagem de uma árvore de decisão simplificada utilizando quatro padrões de projeto: **Composite**, **State**, **Iterator** e **Visitor**.  
O objetivo não é implementar um algoritmo real, mas sim demonstrar a estrutura e o funcionamento dos padrões por meio de *prints*.

---

##  Estrutura do Projeto

### **tree_design.py**
Contém toda a arquitetura do sistema:
- Estrutura hierárquica da árvore (Composite)
- Estados de construção (State)
- Iteradores para navegação (Iterator)
- Visitantes para operações independentes (Visitor)

### **tree_demo.py**
Demonstra o uso da árvore:
- Construção mockada
- Transições entre estados
- Percurso por pré-ordem e BFS
- Aplicação dos visitantes

---

##  Padrões de Projeto Utilizados

### **Composite**
Modela a estrutura da árvore com nós internos e nós folha.

### **State**
Controla o processo de construção da árvore com estados como divisão, parada e poda.

### **Iterator**
Permite percorrer a árvore sem expor a estrutura interna.

### **Visitor**
Aplica operações independentes à árvore, como contagem de folhas ou calcular profundidade.
 

