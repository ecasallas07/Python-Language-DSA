
# Function factorial
def recursion(number):
    
    if number == 0: 
        return 1
    return number * recursion(number-1)
    


    
print(recursion(4))

# Explication in spanish

# La recursividad es donde la funcion se llama asi misma.
# En este caso es una funcion factorial, ya que se ejecuta de la siguiente forma:

# si se le pasa el numero 5 esta opera con recursion(5-1)  = 5 * 24 = 120

# entonces recursion(4) hace el mismo proceso  q es numero 4 operando con recursion(4-1) = 24

# entonces recursion(3) hace el mismo proceso que es numero 3 operando con recursion(3-1) = 6

# entonces recursion(2) hace el mismo proceso que es numero 2 operando con recursion(2-1) = 2

# entonces recursion(1) hace el mismo proceso que es numero 1 operando con recursion(1-1) = 1

# Y se opera hasta recursion(1) ya que si es 0 no llama nuevamente a la funcion sino retorna 1 = 1


# RECURSION

# - Each recursive call requires extra space on the stack frame (memory)
# - A function calls itself with different arguments until a condition is met.


# ITERATION

#-  Each iteration does not require extra space.
#- use control structures such as loops (for,while) to repeat a sequence of instructions until a condition is met


# Example algorithms

# Fibonacci Series, Factorial Finding
# • Merge Sort, Quick Sort
# • Binary Search
# • Tree Traversals and many Tree Problems: InOrder, PreOrder PostOrder
# • Graph Traversals: DFS [Depth First Search] and BFS [Breadth First Search]
# • Dynamic Programming Examples
# • Divide and Conquer Algorithms
# • Towers of Hanoi
# • Backtracking Algorithms [we will discuss in next section]
