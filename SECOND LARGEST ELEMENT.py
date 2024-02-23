def second_largest_element(array):
    n = len(array)
    largest = array[0]
    sec_largest = float("-inf")
    
    for i in range(1,n):
        if array[i] > largest:
            sec_largest = largest 
            largest = array[i]
        elif array[i] > sec_largest and array[i] != largest:
            sec_largest = array[i]
            
    return sec_largest

print("Second Largest: ",second_largest_element([22,3,7,9,100,1]))