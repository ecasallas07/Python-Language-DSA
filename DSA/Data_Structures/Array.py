#reverse array
def reverseArray(arr):
    n = len(arr)
    
    temp = [0] * n
    
    
    for i in range(n):
        temp[i] = arr[ n - i -1]
        
        
    for i in range(n):
        arr[i]=temp[i]
        
if __name__ == '__Array__':
    arr = [1,4,3,2,6,5]
    reverseArray(arr)
    
    
    for i in range(len(arr)):
        print(arr[i],end="")              
    