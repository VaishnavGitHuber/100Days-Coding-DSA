def max_element(array):
    n = len(array)
    max_number = array[0]
    
    for i in range(1,n):
        if array[i] > max_number:
            max_number = array[i] 
        
    return max_number

print("Maximum element in the Array: ",max_element([3,8,9,19]))