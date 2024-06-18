def test(n):
    j = 1 # --> 1 time = O(1)
    for i in range(1,int(n/3)):  # --> n times = O(n)
        print(f"value in i {i}")
        for j in range(1,n,j+4): # --> n time = O(n) because the growth is linear
            print(f" value in j: {j}")
            print(j+ 4)
# Complexity is = 1 x n x n = O(n^2) 
#test(15)          



# Exmaples analysys code

# Algortihm 1: Linear  Search

def linear_search(arr,target):
    for i in range(len(arr)): # --> time = O(n) record n attemps to array
        if arr[i] == target: # --> time  = O(1) in the worst case not find the element
            return i
    return -1    # --> time = O(1)


# Complexity Time = n  x 1 x 1 = O(n)


# Algortihm 2: Binary Search

def binar_search(array,traget):
    
    min = 0    # time --> O(1)
    max = len(array) -1  # time  --> O(1)
    
    while min <= max: # --> time -->O(log n) in each iterattion divide for 2  // en cada iteration lo hace diviendo el array
        mid = (min + max) // 2
        if array[mid] == traget: # --> time O(1)
            return mid
        elif array[mid] < traget:   # --> time O(1)
            min = mid + 1
        elif array[mid] > traget: # --> time  O(1)
            max = mid - 1
            
    return -1    
    
# complexity time 1 x 1 x 1 x 1 x log n = O(log n) Divide el array en la busqueda
 
