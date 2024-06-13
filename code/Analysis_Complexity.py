def test(n):
    j = 1 # --> 1 time = O(1)
    for i in range(1,int(n/3)):  # --> n times = O(n)
        print(f"value in i {i}")
        for j in range(1,n,j+4): # --> n time = O(n) because the growth is linear
            print(f" value in j: {j}")
            print(j+ 4)
# Complexity is = 1 x n x n = O(n^2) 
#test(15)          




def log(n):
    i = n
    for i in range(n):
        i = i /2    
        print(i)
log(4)
