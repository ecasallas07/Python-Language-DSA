import random

#requirements
"""
Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once.

"""

characters = ['c' , 'a' , 't' , 'd', 'o' , 'g']

# options
# random.shuffle(characters)



# solution: This solution is base in recursive programming
def toString(List):
    return ''.join(List)



def permute(list_arr,counter,count_list):
    
    if counter == count_list:
        print(toString(list_arr))
    else:
        for i in range(counter,count_list + 1):
            # print( list_arr[counter],list_arr[i])
            list_arr[counter],list_arr[i] = list_arr[i], list_arr[counter]
            permute(list_arr,counter+1,count_list)
            list_arr[counter], list_arr[i] = list_arr[i], list_arr[counter]

print(permute(characters,0,len(characters)-1))