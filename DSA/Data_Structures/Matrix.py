
# Writting code is art

# Defining number of rows and columns in matrix
rows = 3
cols = 3

# Declaring a matrix of size 3 X 3, and 
# initializing it with value zero
rows, cols = (3, 3)
arr = [[0]*cols]*rows
print(arr)

# Example access a matrix
arr_example = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements of 2-D array
print("First element of first row:", arr_example[0][0])
print("Third element of second row:", arr_example[1][2])
print("Second element of third row:", arr_example[2][1])


# searching matrix

# Function to search for an element in a 2-D list
def search_in_matrix(arr_m, x):
    rows_i, cols_i = len(arr_m), len(arr_m[0])

    # Traverse each row and column
    for i in range(rows_i):
        for j in range(cols_i):
            if arr[i][j] == x:
                return True
    return False

# Driver code to test the function
x_x = 8
arr_m = [
    [0, 6, 8, 9, 11],
    [20, 22, 28, 29, 31],
    [36, 38, 50, 61, 63],
    [64, 66, 100, 122, 128]
]

if search_in_matrix(arr_m, x_x):
    print("YES")
else:
    print("NO")