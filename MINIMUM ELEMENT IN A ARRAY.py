def min_element(array):
    n = len(array)
    min_number = array[0]
    
    for i in range(1,n):
        if array[i] < min_number:
            min_number = array[i]
    
    return min_number

print("Minimum element: ",min_element([3,9,1,7,10,0]))